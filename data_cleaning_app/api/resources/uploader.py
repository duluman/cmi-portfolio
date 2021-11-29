import json

from flask_restful import Resource, request
from flask import Response

from data_cleaning_app.csvparser import CsvParser
from data_cleaning_app.repository import connect, create_table


class Uploader(Resource):
    DB_FILE = None

    @classmethod
    def set_database_file(cls, filename):
        cls.DB_FILE = filename

    def post(self):
        request_data = request.json
        table_name = request_data.get('table_name')
        if table_name is None:
            err = {
                'error': 'Missing table name.'
            }
            return Response(json.dumps(err), status=400, content_type='application/json')

        data = request_data.get('data')
        if data is None:
            err = {
                'error': 'Missing data.'
            }
            return Response(json.dumps(err), status=400, content_type='application/json')

        csv_parser = CsvParser(data)
        columns = csv_parser.to_dataframe().get_columns().get_column_types()
        conn = connect(self.DB_FILE)
        create_table(conn, table_name, columns)
        conn.close()
