import json

from flask import request, Response
from flask_restful import Resource

from data_cleaning_app.aggregators import Aggregator
from data_cleaning_app.repository import connect


class MeanAggregator(Resource):

    @classmethod
    def set_database_file(cls, filename):
        cls.DB_FILE = filename

    def post(self):
        body = request.json
        # extract table name from request body
        table_name = body.get("table_name", None)
        if table_name is None:
            error = {
                "error": "--Failed to compute mean. Missing table_name property."
            }
            return Response(json.dumps(error), status=400, content_type='application/json')

        # extract column names from request body
        columns = body.get("columns", None)

        try:
            # connect to a database
            conn = connect(self.DB_FILE)

            # compute mean for required columns
            agg = Aggregator(conn, table_name, columns)
            columns_means = agg.mean()

            # return a response with the mean per column
            response = {
                "data": columns_means
            }
            return Response(json.dumps(response), status=200, content_type="application/json")
        except Exception as e:
            error = {
                "error": f"--Failed to compute mean. Cause: {e}"
            }
            return Response(json.dumps(error), status=500, content_type="application/type")