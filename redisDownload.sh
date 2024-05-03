#!/bin/bash

# Connect to your Redis server using redis-cli
redis-cli --csv keys '*' | while read key; do
    # For each key, get its value from Redis
    value=$(redis-cli GET "$key")
    # Output key and value to CSV file
    echo "$key,$value"
done > redis_data.csv

