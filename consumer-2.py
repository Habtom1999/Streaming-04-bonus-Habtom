"""
   This script acts  as a message consumer for a RabbitMQ queue named 'first_queue.' 
   It processes incoming messages, performs a transformation on numeric values, 
   and writes the results to a CSV file ('data-result2.csv').
 

    Author: Habtom Woldu
 
    Date: May 22, 2024

"""



import pika
import csv
import sys

def callback(ch, method, properties, body):
    # Process the message ( change to uppercase)
    original_value = body.decode('utf-8')
    transformed_value = original_value * 2
    
    # Write the result to data-result2.csv
    with open('data-result2.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([original_value, transformed_value])

    print(f" [x] Processed message: '{original_value}' => '{transformed_value}'")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# define a main function to run the program
def main():

    try:
         connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
         channel = connection.channel()
         channel.queue_declare(queue='second_queue', durable=True)
         channel.basic_qos(prefetch_count=1)
         channel.basic_consume(queue='second_queue', on_message_callback=callback)
    
         print(" [*] Waiting for messages in consumer2. To exit, press CTRL+C")
         channel.start_consuming()
    except KeyboardInterrupt:
      print("Exiting the consumer.")
    sys.exit(0)

if __name__ == '__main__':
    main()