import json

import pika

# create a connection to RabbitMq
credentials = pika.PlainCredentials(username='', password='')
params = pika.ConnectionParameters(host='', port=5672, virtual_host='', credentials=credentials)
conn = pika.BlockingConnection(params)

# start a channel
channel = conn.channel()

# declare a queue in case it doesn't exist
channel.queue_declare(queue='sewp')

# send message
for i in range(100):
    body = {
        'name': 'my name',
        'location': 'loc',
        'message_num': i
    }
    body = json.dumps(body).encode('gbk')
    channel.basic_publish(exchange='amq.direct',
                          routing_key='sewp-key',
                          body=body)

# close connection
conn.close()
