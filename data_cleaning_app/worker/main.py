import os

from data_cleaning_app.worker.callbacks import process_message
from data_cleaning_app.consumer_base import ConsumerBase

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

