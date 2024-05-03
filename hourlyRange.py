import redis
import matplotlib.pyplot as plt

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Retrieve all keys
keys = redis_client.keys('*')

# Calculate salary ranges
salary_ranges = [float(redis_client.hget(key, 'hourly_high')) - float(redis_client.hget(key, 
'hourly_low')) for key in keys if redis_client.hget(key, 'hourly_high') and 
redis_client.hget(key, 'hourly_low')]

# Plot the histogram
plt.hist(salary_ranges, bins=range(0, 101, 5), color='skyblue', edgecolor='black')
plt.xlabel('Salary Range')
plt.ylabel('Frequency')
plt.title('Distribution of Salary Ranges')
plt.xticks(range(0, 101, 5))
plt.grid(True)
plt.tight_layout()
plt.show()

