"""
    This program sends a message to a queue on the RabbitMQ server.
    It gets the message by reading from a csv file. Sends a line from the csv file. 
   

    Author: Habtom Woldu 
  
    Date: May 22, 2024

"""

import pika
import webbrowser
import csv



"Changed code so it does not ask yes or no question everytime it runs."
def offer_rabbitmq_admin_site(show_offer):
    """Offer to open the RabbitMQ Admin website"""
    if show_offer == True:
        ans = input("Would you like to monitor RabbitMQ queues? y or n ")
        print()
        if ans.lower() == "y":
            webbrowser.open_new("http://localhost:15672/#/queues")
            print()

def send_to_queue(queue_name, message):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        host (str): the host name or IP address of the RabbitMQ server
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue
    """

     # create a blocking connection to the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
     # use the connection to create a communication channel
    channel = connection.channel()
    # use the channel to declare a durable queue
    # a durable queue will survive a RabbitMQ server restart
    # and help ensure messages are processed in order
    # messages will not be deleted until the consumer acknowledges
    channel.queue_declare(queue=queue_name, durable=True)
    # use the channel to publish a message to the queue
    # every message passes through an exchange
    channel.basic_publish(exchange='', routing_key=queue_name, body=message,
                          properties=pika.BasicProperties(delivery_mode=2))
     # print a message to the console for the user
    print(f" [x] Sent '{message}' to {queue_name}") 
    
   
 
        # close the connection to the server
    connection.close()

def main():
    # Read the CSV file and send values to the respective queues
    with open('Life expectancy.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            column1_value = row[0]
            column2_value = row[4]
            send_to_queue('first_queue', column1_value)
            send_to_queue('second_queue', column2_value)

          
    
if __name__ == '__main__':
    main()