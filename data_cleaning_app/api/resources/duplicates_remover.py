import json

from flask import Response
from flask_restful import Resource

from data_cleaning_app.data_cleaning import DataCleaner
from data_cleaning_app.repository import connect


class DuplicatesRemover(Resource):
    DB_FILE = None

    @classmethod
    def set_database_file(cls, filename):
        cls.DB_FILE = filename

    def delete(self, table_name):
        try:
            conn = connect(self.DB_FILE)
            dc = DataCleaner(conn, table_name)
            dc.remove_duplicates()
            conn.close()
            return Response(status=200, content_type="application/json")
        except Exception as e:
            error = {
                "error": f"--Failed to remove duplicates. {e}."
            }
            return Response(json.dumps(error), status=500, content_type="application/json")