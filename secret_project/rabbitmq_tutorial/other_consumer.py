import os

from secret_project.rabbitmq_tutorial.ConsumerBase import ConsumerBase


def process_message(ch, method, properties, body):
    if properties.type == "MessageType2":
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Consumer #2. This is a message of type {properties.type}. {body}")
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


# create a connection to RabbitMq
username = os.environ['CMI_SEWP_RABBIT_USERNAME']
password = os.environ['CMI_SEWP_RABBIT_PASSWORD']
host = os.environ['CMI_SEWP_RABBIT_HOST']
virtual_host = os.environ['CMI_SEWP_RABBIT_VHOST']

consumer = ConsumerBase(username, password, host, virtual_host, 'sewp')
consumer.callback = process_message
consumer.consume()
