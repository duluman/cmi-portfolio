import pika


def process_message(ch, method, properties, body):
    print(type(properties.type), properties.type)
    if properties.type == '1':
        print(body)
    else:
        print("Unknown message")


# create a connection to RabbitMq
credentials = pika.PlainCredentials(username='', password='')
params = pika.ConnectionParameters(host='', port=5672, virtual_host='', credentials=credentials)
conn = pika.BlockingConnection(params)

# start a channel
channel = conn.channel()

# declare a queue in case it doesn't exist
channel.queue_declare(queue='sewp')

channel.basic_consume(queue='sewp', on_message_callback=process_message, auto_ack=True)

channel.start_consuming()
