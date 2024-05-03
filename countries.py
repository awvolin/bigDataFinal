import redis
import matplotlib.pyplot as plt
from collections import Counter

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Retrieve all keys
keys = redis_client.keys('*')

# Extract countries from keys
all_countries = [redis_client.hget(key, 'country').decode('utf-8') for key in keys if 
redis_client.hget(key, 'country')]

# Count country frequencies
country_counts = Counter(all_countries)

# Find top 10 most frequently appearing countries
top_countries = country_counts.most_common(10)

# Extract top countries and their frequencies
top_country_labels = [country[0] for country in top_countries]
top_country_counts = [country[1] for country in top_countries]

# Plot the top 10 countries and their frequencies
plt.bar(top_country_labels, top_country_counts)
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.title('Top 10 Appearing Countries')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

