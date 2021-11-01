import os
import json

from secret_project.repository.repo import MongoRepository

connection_string = os.environ["MONGO_CONN_STRING"]
db_name = os.environ["MONGO_DB_NAME"]
collection_name = os.environ["MONGO_COLLECTION"]

product_repository = MongoRepository(conn_string=connection_string,
                                     db_name=db_name,
                                     collection_name=collection_name)

# sample interaction with json configs
with open("config.json", "r") as config_file:
    config = json.load(config_file)

print(f"Config info {config['database']}")

config["database"]["name"] = "sample 2"
with open("config.json", "w") as config_file:
    json.dump(config, config_file)