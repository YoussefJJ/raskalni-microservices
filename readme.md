# Raskalni Microservices
This is the Raskalni microserices application.
Raskalni is a company that aims to organize the employment of the "Barbechas", by hiring them and making them available to various clients in order to give them more secure working conditions.

## Usage

1- Run the `Kafka` and `Zookeeper` services by running the following command:
```sh
docker-compose up -d
```
2- Run the Requirement Service
```sh
pip install -r requirements.txt
python main.py
```
3- Run the Announcement Service
```sh
pip install -r requirements.txt
python main.py
```
4- Run the Barbecha Acceptance Service
```sh
make init
make start
```
5- Run the Barbecha Insurance Service
```sh
make init
make start
```

6- Finally test the application by running the following command:
```sh
curl -X POST \
  'http://localhost:5000' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "age": 25,
  "sex": "Male",
  "experience": 2,
  "salary": 10000,
  "duration": 2
}'
```
