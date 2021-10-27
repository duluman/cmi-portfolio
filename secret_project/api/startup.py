import os

from secret_project.repository.repo import MongoRepository


connection_string = os.environ["MONGO_STRING"]
db_name = os.environ["MONGO_DB_NAME"]
collection_name = os.environ["MONGO_COLLECTION"]

product_repository = MongoRepository(conn_string=connection_string, db_name=db_name, collection_name=collection_name)
