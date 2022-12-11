from flask import Flask, request
import json
from datetime import datetime
from kafka import KafkaProducer
from fpdf import FPDF

app = Flask(__name__)

# Create a Kafka producer to send data to a Kafka topic
producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.route('/', methods=['POST'])
def handle_post_request():
    # Get the request data as a JSON object
    req_data = request.get_json()
    
    # Extract the fields from the request data
    age = req_data['age']
    sex = req_data['sex']
    experience = req_data['experience']
    salary = req_data['salary']
    duration = req_data['duration']

    # Add a timestamp and sender information to the data
    data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'sender': request.remote_addr,
        'age': age,
        'sex': sex,
        'experience': experience,
        'salary': salary,
        'duration': duration
    }

    # Send the data to a Kafka topic
    producer.send('my-topic', json.dumps(data).encode('utf-8'))

    # Format the data as a PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, f'Age: {age}')
    pdf.cell(40, 10, f'Sex: {sex}')
    pdf.cell(40, 10, f'Experience: {experience}')
    pdf.cell(40, 10, f'Salary: {salary}')
    pdf.cell(40, 10, f'Duration: {duration}')
    pdf.output('data.pdf', 'F')

    # Return a response to the client
    return json.dumps({
        'success': True
    })

if __name__ == '__main__':
    app.run()
