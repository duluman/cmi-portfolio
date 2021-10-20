from flask import Flask, request
from flask_restful import Resource, Api

from python_mongo import MongoMediator


my_flask_app = Flask(__name__)
my_first_api = Api(my_flask_app)

conn_str = "mongodb+srv://admin:parola21212121@cmisewpcluster.wpkvh.mongodb.net/cmiswep?retryWrites=true&w=majority"
# connect to database
mongo = MongoMediator(conn_string=conn_str, db_name="cmiswep", collection_name="sample")

class HelloWorld(Resource):
    def get(self):
        mongo.set_collection("users")
        users = mongo.get_all()
        return users
        
    def post(self):
        data = request.json
        mongo.set_collection("users")
        mongo.insert_one(data)
        return 


# my_first_api.add_resource(HelloWorld, "/users/<int:id>")
my_first_api.add_resource(HelloWorld, "/users")

if __name__ == "__main__":
    my_flask_app.run(debug=True)
