import json
import random
from dataclasses import field
from typing import List, Union

from bson import json_util
from pymongo import MongoClient


class MongoMediator:
    def __init__(self, conn_string: str = None, db_name: str = "cmiswep", collection_name: str = "sample"):
        self.__client = MongoClient(conn_string)
        self.__database_name = db_name
        self.__collection_name = collection_name

    def set_collection(self, collection_name: str):
        """Sets a collection to store elements for the current object state.
        Args:
            collection_name: string - The collection name you want to be set.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  mongo.set_collection('example_collection')
        """
        self.__collection_name = collection_name

    def get_all(self) -> List[dict]:
        """Get all documents from the currently set collection.
        Args:
            None.
        Returns:
            List[dict]: response - The list of documents from the repositories.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  response = mongo.get_all()
        """
        search_query = {}
        projection = {"_id": 0}

        db_result = list(self.__client[self.__database_name][self.__collection_name].find(search_query, projection))

        response = json.loads(json_util.dumps(db_result))

        return response

    def insert_one(self, document: dict = None):
        """Insert one document into the currently set collection.
        Args:
            document: dict - The document you want inserted into the repositories.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  document = {
                      'id': 1
                  }
                  mongo.insert_one(document)
        """
        self.__client[self.__database_name][self.__collection_name].insert_one(document)

    def insert_many(self, documents: List[dict] = field(default_factory=list), validators: List[callable] = field(default_factory=list)):
        """Insert many documents into the currently set collection.
        Args:
            documents: List[dict] - The documents you want inserted into the repositories.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  documents = [{
                      'id': 1
                  }]
                  mongo.insert_many(documents)
                  :param documents:
        """
        for di in documents:
            for validator in validators:
                di = validator(di)
        
        self.__client[self.__database_name][self.__collection_name].insert_many(documents)

    def delete_one(self, id: str):
        self.__client[self.__database_name][self.__collection_name].delete_one({"_id": id})

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
        

if __name__ == "__main__": 
    from pprint import pprint 
    from datetime import datetime

    conn_str = ""
    # connect to database
    mongo = MongoMediator(conn_string=conn_str, db_name="cmiswep", collection_name="sample")

    # mongo.delete_many("email", "andrei@me.com")

    # insert in sample 3 users
    users = [
        {
            "name": "andrei",
            "email": "e@m.c"
        },
        {
            "name": "liviu",
            "email": "a@m.c"
        },
        {
            "name": "luchici",
            "email": "l@m.c"
        },
    ]
    # mongo.insert_many(users)

    # create a new collection + insert 5 actions for our users
    actions = [
        {
            "email": "e@m.c",
            "action": "click-on-save",
            "created_at": datetime.utcnow()
        },
        {
            "email": "e@m.c",
            "action": "click-on-open",
            "created_at": datetime.utcnow()
        },
        {
            "email": "e@m.c",
            "action": "click-on-delete",
            "created_at": datetime.utcnow()
        },
        {
            "email": "e@m.c",
            "action": "click-on-new",
            "created_at": datetime.utcnow()
        }
    ]
    mongo.set_collection("actions_memory_filter")
    # mongo.insert_many(actions)

    # join in memory
    mongo.set_collection("sample")
    users = mongo.get_all()

    mongo.set_collection("actions_memory_filter")
    actions = mongo.get_all()

    users_actions_full = []
    for u in users:
        user_actions = list(filter(lambda x: x["email"] == u["email"], actions))
        for ua in user_actions:
            ua["name"] = u["name"]
        users_actions_full += user_actions

    pprint(users_actions_full)

    def name_validator(d):
        # check field
        if "name" not in d.keys():
            d["name"] = "default name"
        return d 

    def created_at_validator(d):
        if "created_at" not in d.keys():
            d["created_at"] = datetime.utcnow()
        return d
        
    u = [
        {
            "email": 'b@c.com'
        },
        {
            "email": 'c@c.c'
        },
        {
            "email": 'd@d.c',
            "created_at": datetime.utcnow(),
            'name': 'andrei'
        }
    ]

    mongo.set_collection("users_with_validation")
    mongo.insert_many(u, [name_validator, created_at_validator])

    f = {
        "mongo": MongoMediator
    }
    m = f["mongo"]()
        