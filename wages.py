import redis
import matplotlib.pyplot as plt

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Retrieve all keys
keys = redis_client.keys('*')

# Extract hourly high values from keys
hourly_high_values = [float(redis_client.hget(key, 'hourly_high')) for key in keys if 
redis_client.hget(key, 'hourly_high')]

# Plot the histogram
plt.hist(hourly_high_values, bins=range(0, 201, 10), color='skyblue', edgecolor='black')
plt.xlabel('Hourly High')
plt.ylabel('Frequency')
plt.title('Distribution of Hourly High Values')
plt.xticks(range(0, 201, 10))
plt.grid(True)
plt.tight_layout()
plt.show()

