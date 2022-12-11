from kafka import KafkaConsumer
import sys
import sqlite3
import json


# Create a Kafka consumer to read data from a Kafka topic
consumer = KafkaConsumer('barbecha-acceptance-topic',
                         bootstrap_servers=['localhost:9092'])
# connect to database
conn = sqlite3.connect('data.db')

# create table if not exists
# For the status it's either accepted 'A', or rejected 'R'
conn.execute('''CREATE TABLE IF NOT EXISTS data
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            sex TEXT,
            age INTEGER,
            experience INTEGER,
            salary double,
            duration INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT CHECK ( status IN ('A', 'R') ) NOT NULL
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

    # Extract infromation
    age = data['age']
    sex = data['sex']
    experience = data['experience']
    salary = data['salary']
    duration = data['duration']
    timestamp = data['timestamp']
    status = 'A' if salary < 2000 else 'R'

    # # save object to database
    conn.execute("INSERT INTO data (age, sex, experience, salary, duration, timestamp, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (age, sex, experience, salary, duration, timestamp, status))
    conn.commit()

sys.exit()
