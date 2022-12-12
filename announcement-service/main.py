from kafka import KafkaConsumer, KafkaProducer
import sys
import sqlite3
import json


# Create a Kafka consumer to read data from a Kafka topic
consumer = KafkaConsumer('my-topic', bootstrap_servers=['localhost:9092'])
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'])
# connect to database
conn = sqlite3.connect('data.db')

# create table if not exists
conn.execute('''CREATE TABLE IF NOT EXISTS data
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
    # # save object to database
    age = data['age']
    sex = data['sex']
    experience = data['experience']
    salary = data['salary']
    duration = data['duration']
    description = data['description']
    timestamp = data['timestamp']

    conn.execute("INSERT INTO data (age, sex, experience, salary, duration, description, timestamp) VALUES (?, ?, ?, ?, ?,? , ?)",
                 (age, sex, experience, salary, duration, description, timestamp))
    conn.commit()

    # In our case the employee is a barbech
    employee = {
        "age": age,
        "sex": sex,
        "experience": experience,
        "salary": salary,
        "duration": duration,
        "description": description,
        "timestamp": timestamp
    }
    print(employee)
    producer.send('barbecha-acceptance-topic',
                  json.dumps(employee).encode('utf-8'))


sys.exit()
