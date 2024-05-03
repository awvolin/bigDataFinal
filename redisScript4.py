import csv
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)
csv_file = 'kaggle_set.csv'

# Open the CSV file and read its contents
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    # Iterate over each row in the CSV
    for row in reader:
        # Create a unique identifier for each job listing
        title = row['title']

        # Store the job listing data as a hash in Redis
        redis_client.hmset(title, row)

print("CSV data imported into Redis successfully")

