from kafka import KafkaConsumer
import sys
import sqlite3
import json


# Create a Kafka consumer to read data from a Kafka topic
consumer = KafkaConsumer('insurance-topic',
                         bootstrap_servers=['localhost:9092'])
# connect to database
conn = sqlite3.connect('insurance.db')

# create table if not exists
conn.execute('''CREATE TABLE IF NOT EXISTS employees
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            sex TEXT,
            age INTEGER,
            experience INTEGER,
            salary double,
            duration INTEGER,
            description TEXT,
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

    # Extract infromation
    age = data['age']
    sex = data['sex']
    experience = data['experience']
    salary = data['salary']
    duration = data['duration']
    description = data['description']
    timestamp = data['timestamp']

    # # save object to database
    conn.execute("INSERT INTO employees (age, sex, experience, salary, duration, description, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (age, sex, experience, salary, duration, description, timestamp))
    conn.commit()

sys.exit()
