import os

from flask import Flask
from flask_restful import Api

from data_cleaning_app.api.resources.duplicates_remover import DuplicatesRemover
from data_cleaning_app.api.resources.nulls_remover import NullsRemover
from data_cleaning_app.api.resources.uploader import Uploader

app = Flask(__name__)
api = Api(app)

dbfile = os.environ.get("DB_FILE")
Uploader.set_database_file(dbfile)
DuplicatesRemover.set_database_file(dbfile)
NullsRemover.set_database_file(dbfile)

api.add_resource(Uploader, '/api/v1/upload')
api.add_resource(DuplicatesRemover, '/api/v1/remove-duplicates/<string:table_name>')
api.add_resource(NullsRemover, '/api/v1/remove-nulls/<string:table_name>')

if __name__ == "__main__":
    app.run(debug=True, port=3004)
