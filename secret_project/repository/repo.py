import json
from typing import List, Union

from bson import json_util
from pymongo import MongoClient


class MongoRepository:
    def __init__(self, conn_string: str = None,
                 db_name: str = "cmiswep",
                 collection_name: str = "products"):
        self.__client = MongoClient(conn_string)
        self.__database_name = db_name
        self.__collection_name = collection_name

    def set_database(self, database_name: str):
        self.__database_name = database_name

    def set_collection(self, collection_name: str):
        self.__collection_name = collection_name

    def get_all(self, projection=None) -> List[dict]:
        search_query = {}
        if projection is None:
            projection = {"_id": 0}

        db_result = list(
            self.__client[self.__database_name][self.__collection_name].find(
                search_query, projection))

        response = json.loads(json_util.dumps(db_result))

        return response

    def get_by_field_value(self, field, value, projection=None) -> List[dict]:
        search_query = {
            field: value
        }
        if projection is None:
            projection = {"_id": 0}

        db = self.__client[self.__database_name]
        collection = db[self.__collection_name]

        results = list(collection.find(search_query, projection))
        results_dict = json.loads(json_util.dumps(results))

        return results_dict

    def insert_one(self, document: dict = None):

        self.__client[self.__database_name][self.__collection_name].insert_one(
            document)

    def insert_many(self, documents):

        self.__client[self.__database_name][self.__collection_name].insert_many(
            documents)

    def update_one_by_field(self, document: dict = None, field: str = None):
        search_query = {
            field: document[field]
        }
        db = self.__client[self.__database_name]
        col = db[self.__collection_name]
        col.update_one(search_query, document)

    def delete_one(self, id: str):
        db = self.__client[self.__database_name]
        col = db[self.__collection_name]
        col.delete_one({"_id": id})

    def delete_many(self, field: str, value: Union[str, int]):
        db = self.__client[self.__database_name]
        col = db[self.__collection_name]
        col.delete_many({field: value})

    def delete_many_by_id(self, ids: List[str]):
        db = self.__client[self.__database_name]
        col = db[self.__collection_name]
        delete_filter = {
            "_id": {
                "$in": ids
            }
        }
        col.delete_many(delete_filter)
