import csv
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)
csv_file = 'kaggle_set.csv'

# Open the CSV file and read its contents
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    # Iterate over each row in the CSV
    for row in reader:
        title = row['title']
        link = row['link']
        published_date = row['published_date']
        is_hourly = row['is_hourly']
        hourly_low = row['hourly_low']
        hourly_high = row['hourly_high']
        budget = row['budget']
        country = row['country']

        redis_client.set(f"title:{title}", title)
        redis_client.set(f"link:{title}", link)
        redis_client.set(f"published_date:{title}", published_date)
        redis_client.set(f"is_hourly:{title}", is_hourly)
        redis_client.set(f"hourly_low:{title}", hourly_low)
        redis_client.set(f"hourly_high:{title}", hourly_high)	
        redis_client.set(f"budget:{title}", budget)
        redis_client.set(f"country:{title}", country)

print("CSV data imported into Redis successfully")
