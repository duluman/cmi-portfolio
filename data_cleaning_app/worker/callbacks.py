import os
from sqlite3 import connect
from time import sleep
import uuid

from data_cleaning_app.repository import get_data_for_desired_columns, store_task_result
from data_cleaning_app.worker.producer import channel, send_task_started_message


def generate_task_id():
    return uuid.uuid1()


def process_message(ch, method, properties, body):
    message_type = properties.type
    if message_type == "ComputeMeanRequest":
        ch.basic_ack(delivery_tag=method.delivery_tag)
        task_id = generate_task_id()

        # send message to RabbitMQ that we are processing the request
        send_task_started_message(channel, task_id, "ComputeMeanResponse")

        # start processing
        try:
            result = compute_mean(body)

            # store result + task_id in the tasks tables
            dbfile = os.environ.get("DB_FILE")
            conn = connect(dbfile)
            store_task_result(conn, task_id, result)
            conn.close()
        except Exception as e:
            # store error + task_id in the tasks table
            error = {
                "error": f"Failed to compute mean. Reason: {e}"
            }
            dbfile = os.environ.get("DB_FILE")
            conn = connect(dbfile)
            store_task_result(conn, task_id, error)
            conn.close()
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


def compute_mean(body):
    table_name = body.get("table_name", None)
    columns = body.get("columns", None)

    dbfile = os.environ.get("DB_FILE")
    conn = connect(dbfile)
    data = get_data_for_desired_columns(conn, table_name, columns)
    conn.close()

    # compute mean. TODO: VEEEERY INEFFICIENT. NEEDS REFACTORING. JUST ILLUSTRATES A POINT.
    # initialize a list with zeros. One value for each column available
    means = []
    for _ in data[0]:
        means.append(0)

    # compute mean by adding values one by one to each column
    for row in data:
        for column_index, value in enumerate(row):
            sleep(1)
            means[column_index] = means[column_index] + value
        sleep(1)

    for i in range(len(means)):
        means[i] = means[i] / len(data)

    result = {
        "data": means
    }

    return result






