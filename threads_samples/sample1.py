import os
import json
import datetime

from pika.spec import BasicProperties 

from threads_samples.consumer_base import ConsumerBase


def process_message(ch, method, properties, body):
    message_type = properties.type
    if message_type == "MessageType1":
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Consumer #1. This is a message of type {message_type}. {body}")
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

# create a connection to RabbitMq
username = os.environ['CMI_SEWP_RABBIT_USERNAME']
password = os.environ['CMI_SEWP_RABBIT_PASSWORD']
host = os.environ['CMI_SEWP_RABBIT_HOST']
virtual_host = os.environ['CMI_SEWP_RABBIT_VHOST']

# === Consumer === #
consumer = ConsumerBase(username, password, host, virtual_host, 'sewp')
consumer.callback = process_message

# TODO: 1. run consumer.consume() on a separate thread

# TODO: 4. run 5 consumers on 5 different threads

# === Producer === #
# start a channel
channel = consumer.get_connection().channel()

# declare a queue in case it doesn't exist
channel.queue_declare(queue='sewp')

# declare message types and priorities
message_types = ["MessageType1", "MessageType2"]
priorities = [10, 1]

for i in range(100):

    # create message body
    body = {
        'name': 'my name',
        'location': 'loc',
        'message_num': f"Message number #{i}. This is a very important message."
    }
    body = json.dumps(body).encode('gbk')

    # set message type, timestamp, priority
    message_type = message_types[i % 2]
    timestamp = int(datetime.timestamp(datetime.fromisoformat(datetime.utcnow().isoformat())))
    priority = priorities[i % 2]

    # create message properties 
    properties = BasicProperties(type=message_type, timestamp=timestamp, priority=priority)
    
    # send message 
    channel.basic_publish(exchange='amq.direct',
                          routing_key='sewp-key',
                          properties=properties,
                          body=body)

    # TODO: 2. send messages on a separate thread (1 thread per message)

    # TODO: 3. send messages on a separate thread (1 for all messages)
