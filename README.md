# Streaming-04-bonus-Habtom 
This project demonstrates a data processing pipeline using RabbitMQ with a producer and two consumers.

Author: Habtom Woldu

Date: May 22, 2024

Introduction
The provided Python code is to streamline the processing of data from a multi-column CSV file through the utilization of RabbitMQ queues. This project offers an efficient way to split and process data from an input CSV file and apply specific transformations to the extracted information. By distributing the workload to multiple worker processes, this code demonstrates the power of RabbitMQ in managing concurrent data processing tasks.

# Before You Begin

1. Fork this starter repo into your GitHub.
1. Clone your repo down to your machine.
1. View / Command Palette - then Python: Select Interpreter
1. Select your conda environment.

## Read

1. Read the [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)

Modify the publisher script (publisher.py) to send data to RabbitMQ queues.
Run the publisher  script to populate the queues.
Run consumer1.py and consumer2.py to process the data and write results to CSV files.

# Project Structure

publisher.py: Sends data from data.csv to two RabbitMQ queues.
consumer1.py: Monitors the first queue, performs transformations, and writes to data-result1.csv.
consumer2.py: Monitors the second queue, performs transformations, and writes to data-result2.csv.
data.csv: original csv file, input CSV file with multiple columns.
data-result1.csv: Output CSV file for processed data from consumer 1.
data-result2.csv: Output CSV file for processed data from consumer 2.
README.md: Project documentation.

## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
![alt text](Bonus.png)
![alt text](Bonus-1.png)
![alt text](Bonus-2.png)



