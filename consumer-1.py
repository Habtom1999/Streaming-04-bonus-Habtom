"""
   This program listens to 'second_queue' in RabbitMQ, 
   converts received messages to uppercase, and records both the original and transformed values
   in a CSV file ('data-result1.csv').
 
 

    Author: Habtom Woldu
 
    Date: May 22, 2024

"""

import pika
import csv
import sys

def callback(ch, method, properties, body):
    # Process the message (change to uppercase)
    original_value = body.decode('utf-8')
    transformed_value = original_value.upper()  # This will convert the message to uppercase

    # Write the result to data-result1.csv
    with open('data-result1.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([original_value, transformed_value])

    print(f" [x] Processed message: '{original_value}' => '{transformed_value}'")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='first_queue', durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='first_queue', on_message_callback=callback)

        print(" [*] Waiting for messages in consumer1. To exit, press CTRL+C")
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Exiting the consumer.")
        sys.exit(0)

if __name__ == '__main__':
    main()
