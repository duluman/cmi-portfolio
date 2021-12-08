import json

from flask import Response, request
from flask_restful import Resource

from data_cleaning_app.data_cleaning import DataCleaner
from data_cleaning_app.repository import connect


class NullsReplacer(Resource):
    DB_FILE = None

    @classmethod
    def set_database_file(cls, filename):
        cls.DB_FILE = filename

    def post(self):
        data = request.json
        try:
            conn = connect(self.DB_FILE)
            dc = DataCleaner(conn, data['table_name'])
            dc.replace_nulls(data['value'], data.get('columns', None))
            conn.close()
            return Response(status=200, content_type="application/json")
        except Exception as e:
            error = {
                "error": f"--Failed to replace NULL values. {e}."
            }
            return Response(json.dumps(error), status=500, content_type="application/json")