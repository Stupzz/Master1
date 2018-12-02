import pika
import logging


class MQ_sender:
    def __init__(self, ip_adress):
        """Create new sender for the server on the ip adress"ip_adress" """
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip_adress))
            self.channel = self.connection.channel()
        except ValueError:
            logging.error("Ip adress not found")

    def publish(self, message, exchange):
        """ Publish the message "message" to the queue "routing_key",
            Create the queue if she doesn't exist"""
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type='fanout')

        self.channel.basic_publish(exchange=exchange,
                                   routing_key='',
                                   body=message)

    def close(self):
        """Close the connection with the server"""
        self.connection.close()