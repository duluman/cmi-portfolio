import json
import os
from datetime import datetime

from pika import PlainCredentials, ConnectionParameters, BlockingConnection, BasicProperties

username = os.environ['CMI_SEWP_RABBIT_USERNAME']
password = os.environ['CMI_SEWP_RABBIT_PASSWORD']
host = os.environ['CMI_SEWP_RABBIT_HOST']
virtual_host = os.environ['CMI_SEWP_RABBIT_VHOST']

# create a connection to RabbitMq
credentials = PlainCredentials(username=username, password=password)
params = ConnectionParameters(host=host, port=5672, virtual_host=virtual_host, credentials=credentials)
conn = BlockingConnection(params)

# start a channel
channel = conn.channel()

# declare a queue in case it doesn't exist
channel.queue_declare(queue='sewp')

# send message
message_types = ["MessageType1", "MessageType2"]
priorities = [10, 1]

for i in range(100):
    body = {
        'name': 'my name',
        'location': 'loc',
        'message_num': f"Message number #{i}. This is a very important message."
    }
    message_type = message_types[i % 2]
    timestamp = int(datetime.timestamp(datetime.fromisoformat(datetime.utcnow().isoformat())))
    priority = priorities[i % 2]

    properties = BasicProperties(type=message_type, timestamp=timestamp, priority=priority)
    body = json.dumps(body).encode('gbk')
    channel.basic_publish(exchange='amq.direct',
                          routing_key='sewp-key',
                          properties=properties,
                          body=body)

# close connection
conn.close()

