import os
import json
from datetime import datetime

from pika import PlainCredentials, ConnectionParameters, BlockingConnection
from pika.spec import BasicProperties
import threading

from threads_samples.consumer_base import ConsumerBase


def process_message(ch, method, properties, body):
    message_type = properties.type

    if message_type == "MessageType1":
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Consumer #1. This is a message of type {message_type}. {body}")
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


def process_message2(ch, method, properties, body):
    message_type = properties.type
    if message_type == "MessageType2":
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Consumer #2. This is a message of type {message_type}. {body}")
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


# create a connection to RabbitMq
username = "dzcrqstc" # os.environ['CMI_SEWP_RABBIT_USERNAME']
password = "RI_PflutYKlPTccvbMbkip6k7n22TxvB" # os.environ['CMI_SEWP_RABBIT_PASSWORD']
host = "baboon-01.rmq.cloudamqp.com" # os.environ['CMI_SEWP_RABBIT_HOST']
virtual_host = "dzcrqstc" # os.environ['CMI_SEWP_RABBIT_VHOST']

# === Consumer === #
consumer = ConsumerBase(username, password, host, virtual_host, 'sewp')
consumer.callback = process_message

# TODO: 1. run consumer.consume() on a separate thread. Hint: Fire & forget
thread = threading.Thread(target=consumer.consume, name="RabbitMQ Consumer 0")
thread.start()

# TODO: 4. run 5 consumers on 5 different threads. Hint: Fire & forget
threads = []
for i in range(5):
    consumer = ConsumerBase(username, password, host, virtual_host, 'sewp')
    consumer.callback = process_message
    t = threading.Thread(target=consumer.consume, name=f"RabbitMQ Consumer {i+1}")
    threads.append(t)

for t in threads:
    t.start()

# === Producer === #
# start a channel
# credentials = PlainCredentials(username=username, password=password)
# params = ConnectionParameters(host=host, port=5672, virtual_host=virtual_host, credentials=credentials)
conn = consumer.get_connection()
channel = conn.channel()

# declare a queue in case it doesn't exist
channel.queue_declare(queue='sewp')

# declare message types and priorities
message_types = ["MessageType1", "MessageType2"]
priorities = [10, 1]

for i in range(100000):
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

    # TODO: 2. send messages on a separate thread (1 thread per message). Hint: Fire & forget

    # TODO: 3. send messages on a separate thread (1 for all messages)
