import os

from flask import Flask
from flask_restful import Api

from data_cleaning_app.api.resources.duplicates_remover import DuplicatesRemover
from data_cleaning_app.api.resources.mean_aggregator_long import MeanAggregatorLong
from data_cleaning_app.api.resources.nulls_remover import NullsRemover
from data_cleaning_app.api.resources.nulls_replacer import NullsReplacer
from data_cleaning_app.api.resources.uploader import Uploader
from data_cleaning_app.api.resources.mean_aggregator import MeanAggregator

app = Flask(__name__)
api = Api(app)

dbfile = os.environ.get("DB_FILE")
Uploader.set_database_file(dbfile)
DuplicatesRemover.set_database_file(dbfile)
NullsRemover.set_database_file(dbfile)
NullsReplacer.set_database_file(dbfile)
MeanAggregator.set_database_file(dbfile)
MeanAggregatorLong.set_database_file(dbfile)

api.add_resource(Uploader, '/api/v1/upload')
api.add_resource(DuplicatesRemover, '/api/v1/remove-duplicates/<string:table_name>')
api.add_resource(NullsRemover, '/api/v1/remove-nulls/<string:table_name>')
api.add_resource(NullsReplacer, '/api/v1/replace-nulls')
api.add_resource(MeanAggregator, '/api/v1/mean')
api.add_resource(MeanAggregatorLong, '/api/v1/mean-long', '/api/v1/mean-long/<string:task_id>')


if __name__ == "__main__":
    app.run(debug=True, port=3004)
