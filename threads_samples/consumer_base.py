import os

from pika import PlainCredentials, ConnectionParameters, BlockingConnection


class ConsumerBase:
    def __init__(self, username=None, password=None, host=None, vhost=None, queue=None):
        # create a connection to RabbitMq
        credentials = PlainCredentials(username=username, password=password)
        params = ConnectionParameters(host=host, port=5672, virtual_host=vhost, credentials=credentials)
        self.__conn = BlockingConnection(params)
        self.__queue = queue
        self.callback = None

    def consume(self):
        channel = self.__conn.channel()
        channel.basic_consume(queue=self.__queue, on_message_callback=self.callback, auto_ack=False)
        channel.start_consuming()

    def get_connection(self):
        return self.__conn