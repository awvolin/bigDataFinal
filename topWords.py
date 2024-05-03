import redis
import matplotlib.pyplot as plt
from collections import Counter
import re

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Retrieve all keys
keys = redis_client.keys('*')

# Extract words from keys
all_words = [word.lower() for key in keys for word in re.split(r'[^a-zA-Z0-9]', key.decode('utf-8')) if word]

# Count word frequencies
word_counts = Counter(all_words)

# Exclude single-character words and common stopwords
word_counts = {word: count for word, count in word_counts.items() if len(word) > 1 and word not in ['the', 'and', 'of', 'in', 'for', 'to', 'on', 'with', 'is']}

# Find top 10 most frequently used words
top_words = Counter(word_counts).most_common(10)

# Extract top words and their frequencies
top_word_labels = [word[0] for word in top_words]
top_word_counts = [word[1] for word in top_words]

# Plot the top 10 words and their frequencies
plt.bar(top_word_labels, top_word_counts)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Frequently Used Words in Keys')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
