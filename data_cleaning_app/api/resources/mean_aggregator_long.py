import json

from flask import request, Response
from flask_restful import Resource

from data_cleaning_app.business_logic_producer import send_message, channel
from data_cleaning_app.repository import connect, get_task_result


class MeanAggregatorLong(Resource):
    DB_FILE = None

    @classmethod
    def set_database_file(cls, filename):
        cls.DB_FILE = filename

    def post(self):
        body = request.json
        table_name = body.get("table_name", None)
        columns = body.get("columns", None)

        # send rabbitmq message
        try:
            send_message(channel, table_name, columns)
        except Exception as e:
            error = {
                "error": f"--Failed to start processing. Reason {e}"
            }
            return Response(json.dumps(error), status=200, content_type="application/json")

        # wait until rabbit mq response
        # TODO: Find a solution for this
        # response = get_message()
        response = {}

        # return task_id to client
        return Response(json.dumps(response), status=200, content_type="application/json")

    def get(self, task_id):
        try:
            conn = connect(self.DB_FILE)
            result = get_task_result(conn, task_id)
            conn.close()
            return Response(json.dumps(result), status=200, content_type="application/json")
        except Exception as e:
            error = {
                "error": f"--Failed to get task result. Reason: {e}"
            }
            return Response(json.dumps(error), status=500, content_type="application/json")