import os

from flask import Flask
from flask_restful import Api

from data_cleaning_app.api.resources.uploader import Uploader

app = Flask(__name__)
api = Api(app)

dbfile = os.environ.get("DB_FILE")
Uploader.set_database_file(dbfile)

api.add_resource(Uploader, '/api/v1/upload')

if __name__ == "__main__":
    app.run(debug=True, port=3004)
