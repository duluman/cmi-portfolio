from nightly_workers.worker_consumer import WorkerConsumer

consumer = WorkerConsumer(username=None, password=None, host=None, virtual_host=None, exchange=None, queue=None)
consumer.consume()

