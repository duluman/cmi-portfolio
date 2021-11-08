from datetime import datetime

import pika

from nightly_workers.reporting.average_sensor_reading_report_builder import AverageReadingsReportBuilder
from nightly_workers.worker_producer import WorkerProducer


def callback(ch, method, properties, body):
    producer = WorkerProducer(username=None, password=None, host=None, virtual_host=None, exchange=None)
    if properties.type == 'average':
        report_builder = AverageReadingsReportBuilder()
        message = report_builder.compute_report()
    elif properties.type == 'moving_average':
        # TODO: implement moving average report builder
        message = {}
    else:
        message = {
            "error": "Unknown message type.",
            "timestamp": datetime.utcnow()
        }
    producer.publish(body=message)


class WorkerConsumer:

    def __init__(self, username=None, password=None, host=None, port=5672, virtual_host=None, exchange=None, queue=None):
        # create a connection to RabbitMq
        credentials = pika.PlainCredentials(username=username, password=password)
        self.__params = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host,
                                                  credentials=credentials)
        self.__exchange = exchange
        self.__queue = queue
        self.__conn = None

    def connect(self):
        self.__conn = pika.BlockingConnection(self.__params)

    def consume(self):
        self.connect()
        channel = self.__conn.channel()
        channel.basic_consume(queue=self.__queue, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
