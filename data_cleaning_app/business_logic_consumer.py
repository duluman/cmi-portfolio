import os

from data_cleaning_app.consumer_base import ConsumerBase


def process_message(ch, method, properties, body):
    message_type = properties.type
    if message_type == "ComputeMeanResponse":
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return body
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


# create a connection to RabbitMq
username = os.environ['CMI_SEWP_RABBIT_USERNAME']
password = os.environ['CMI_SEWP_RABBIT_PASSWORD']
host = os.environ['CMI_SEWP_RABBIT_HOST']
virtual_host = os.environ['CMI_SEWP_RABBIT_VHOST']

print("Creating consumer..")
consumer = ConsumerBase(username, password, host, virtual_host, 'sewp', process_message)

print(f"Consumer created {consumer}..")
print("Starting..")
consumer.consume()
