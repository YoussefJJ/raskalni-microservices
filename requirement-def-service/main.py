from flask import Flask, request, jsonify
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
    description = req_data['description']
    # Add a timestamp and sender information to the data
    data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'sender': request.remote_addr,
        'age': age,
        'sex': sex,
        'experience': experience,
        'salary': salary,
        'duration': duration,
        'description': description
    }

    # Send the data to a Kafka topic
    producer.send('my-topic', json.dumps(data).encode('utf-8'))

    # Format the data as a PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    # add title centered, bigger font
    pdf.cell(200, 10, txt='Rasklani', ln=1, align='C')
    # add subtitle
    pdf.cell(200, 10, txt='Recruitment needs', ln=1, align='C')

    pdf.set_font('Arial', '', 12)

    # print data line by line
    for key, value in data.items():
        pdf.cell(200, 10, txt=f'{key}: {value}', ln=1, align='L')

    pdf.output('data.pdf', 'F')

    # Return a response to the client
    return json.dumps({
        'success': True
    })


if __name__ == '__main__':
    app.run()
