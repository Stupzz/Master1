import threading

import pika
import logging


class MQ_receiver:

    def __init__(self, ip_adress, exchange, function_to_call):
        """ Create new receiver of the server who have the ip adress " ip_adress".
            This receiver could only read message from the exchange "exchange".
            When a message is received, the function "function_to_call" is executed"""
        self.function_to_call = function_to_call
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip_adress))
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange=exchange,
                                          exchange_type='fanout')

            result = self.channel.queue_declare(exclusive=True)
            self.queue_name = result.method.queue

            self.channel.queue_bind(exchange=exchange,
                                    queue=self.queue_name)

        except ValueError:
            logging.error("Ip adress not found")

        self.t1 = threading.Thread(target=self.channel.start_consuming)
        self.t1.start()

    def start_reiceive(self):

        def callback(ch, method, properties, body):
            """Executed when a message was received"""
            body = body.decode()
            self.function_to_call(body)

        self.channel.basic_consume(callback,
                                   queue=self.queue_name,
                                   no_ack=True)
        self.channel.start_consuming()

    def close(self):
        self.channel.stop_consuming()
        self.connection.close()
