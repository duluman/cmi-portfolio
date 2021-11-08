import json

import pika


class WorkerProducer:

    def __init__(self, username=None, password=None, host=None, port=5672, virtual_host=None, exchange=None):
        # create a connection to RabbitMq
        credentials = pika.PlainCredentials(username=username, password=password)
        self.__params = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host,
                                                  credentials=credentials)
        self.__exchange = exchange
        self.__conn = None

    def connect(self):
        self.__conn = pika.BlockingConnection(self.__params)

    def publish(self, body=None):
        self.connect()
        body = json.dumps(body).encode('gbk')
        channel = self.__conn.channel()
        channel.basic_publish(exchange=self.__exchange, routing_key='', body=body)
        self.__conn.close()
