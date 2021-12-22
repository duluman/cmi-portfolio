import json

from flask import Response
from flask_restful import Resource

from data_cleaning_app.data_cleaning import DataCleaner
from data_cleaning_app.repository import connect


class NullsRemover(Resource):
    DB_FILE = None

    @classmethod
    def set_database_file(cls, filename):
        cls.DB_FILE = filename

    def delete(self, table_name):
        try:
            conn = connect(self.DB_FILE)
            dc = DataCleaner(conn, table_name)
            dc.remove_rows_with_nulls()
            conn.close()
            return Response(status=200, content_type="application/json")
        except Exception as e:
            error = {
                "error": f"--Failed to remove rows that contain null values. {e}."
            }
            return Response(json.dumps(error), status=500, content_type="application/json")