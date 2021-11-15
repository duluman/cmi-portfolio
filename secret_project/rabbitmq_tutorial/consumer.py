import asyncio
import os

from secret_project.rabbitmq_tutorial.ConsumerBase import ConsumerBase


def process_message(ch, method, properties, body):
    message_type = properties.type
    if message_type == "MessageType1":
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Consumer #1. This is a message of type {message_type}. {body}")
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


async def consume(consumer):
    consumer.consume()
    return

# create a connection to RabbitMq
username = os.environ['CMI_SEWP_RABBIT_USERNAME']
password = os.environ['CMI_SEWP_RABBIT_PASSWORD']
host = os.environ['CMI_SEWP_RABBIT_HOST']
virtual_host = os.environ['CMI_SEWP_RABBIT_VHOST']

consumer = ConsumerBase(username, password, host, virtual_host, 'sewp')
consumer.callback = process_message
t = [consume(consumer)]
print("Running and moved to next line.")
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(t))
