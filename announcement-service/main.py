from kafka import KafkaConsumer
import sys
import sqlite3
import uuid
import json


# Create a Kafka consumer to read data from a Kafka topic
consumer = KafkaConsumer('my-topic', bootstrap_servers=['localhost:9092'])
#connect to database
conn = sqlite3.connect('data.db')

# create table if not exists
conn.execute('''CREATE TABLE IF NOT EXISTS data
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            sex TEXT,
            age INTEGER,
            experience INTEGER,
            salary double,
            duration INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );''')



print('Waiting for messages...')
# Continuously read data from the Kafka consumer
for msg in consumer:
    # Print the data to the console
    print(msg.value)
    # get message and save it to object
    data = msg.value.decode('utf-8')
    data = json.loads(data)
    print(data)
    # # save object to database

    conn.execute("INSERT INTO data (age, sex, experience, salary, duration, timestamp) VALUES (?, ?, ?, ?, ?, ?)", 
    (data['age'], data['sex'], data['experience'], data['salary'], data['duration'], data['timestamp']))
    conn.commit()

sys.exit()