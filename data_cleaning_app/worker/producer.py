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


def send_task_started_message(channel, task_id, message_type):
    body = {
        'status': 'RUNNING',
        'task_id': task_id,
    }
    timestamp = int(datetime.timestamp(datetime.fromisoformat(datetime.utcnow().isoformat())))

    properties = BasicProperties(type=message_type, timestamp=timestamp)
    body = json.dumps(body).encode('gbk')
    channel.basic_publish(exchange='amq.direct',
                          routing_key='sewp-key',
                          properties=properties,
                          body=body)


def send_error_message(channel, task_id, message):
    body = {
        'status': 'ERROR',
        'task_id': task_id,
        'erorr': message
    }
    timestamp = int(datetime.timestamp(datetime.fromisoformat(datetime.utcnow().isoformat())))

    properties = BasicProperties(type="ErrorMessage", timestamp=timestamp)
    body = json.dumps(body).encode('gbk')
    channel.basic_publish(exchange='amq.direct',
                          routing_key='sewp-key',
                          properties=properties,
                          body=body)

