import json
import sqlite3


def connect(dbfile):
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Exception as e:
        print(f"--Failed to connect to the database {dbfile}. Error: {e}.")
        raise e


def create_table(conn, table_name, columns):
    """
        CREATE TABLE [IF NOT EXISTS] [schema_name].table_name (
        column_1 data_type PRIMARY KEY,
        column_2 data_type NOT NULL,
        column_3 data_type DEFAULT 0,
        )
    """
    query = f"CREATE TABLE IF NOT EXISTS {table_name} (" \
            f"{table_name}_id integer PRIMARY KEY AUTOINCREMENT,\n"
    for key, value in columns.items():
        query += f"{key} {value},"
    query = query[:-1]
    query += ");"

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(f"--Failed to create table {table_name}. Error: {e}.")
        raise e


def insert_data(conn, data, table_name, columns):
    # TODO: investigate why strings are inserted as "'value'"
    """
    INSERT INTO {table_name} (col1, col2, ...) VALUES (?, ?, ...)
    columns = {
        column_name: column_type
    }
    data = List[List]
    """
    columns_part = ""
    for key in columns.keys():
        columns_part += f"{key},"
    columns_part = columns_part[:-1]

    values_part = ""
    for i in range(len(columns.keys())):
        values_part += "?,"
    values_part = values_part[:-1]

    query = f"INSERT INTO {table_name} ({columns_part}) VALUES ({values_part})"

    try:
        cursor = conn.cursor()
        for row in data:
            cursor.execute(query, row)
        conn.commit()
    except Exception as e:
        print(f"--Failed to create table {table_name}. Error: {e}.")
        raise e


def get_data(conn, table_name, columns=None):
    """
    if columns == None: SELECT * FROM table_name
    if columns != None: SELECT column1, column2, ..., columnN FROM table_name
    """
    if columns is None:
        selected_columns = "*"
    else:
        selected_columns = ",".join(columns)
    query = f"select {selected_columns} from {table_name}"

    try:
        cursor = conn.cursor()
        data = list(cursor.execute(query))
        return data
    except Exception as e:
        print(f"--Failed to get data from {table_name}. Error: {e}.")
        raise e


def delete_data(conn, table_name, column_name=None, column_value=None):
    """
    if column_name == None: DELETE FROM table_name where <table_name>_id=value
    if column_name != None: DELETE FROM table_name where column_name=value
    """
    if column_value is None:
        print("--Failed to delete data. Column value is none.")
        raise Exception("--Failed to delete data. Column value is none.")

    if column_name is None:
        column = f"{table_name}_id"
    else:
        column = column_name
    query = f"DELETE FROM {table_name} WHERE {column}={column_value}"

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(f"--Failed to delete data for {column}={column_value}. Error: {e}.")
        raise e


def replace_null_by_column(conn, cursor, table_name, columns, value):
    for column in columns:
        try:
            # TODO: investigate why we cannot replace with strings.
            query = f"UPDATE {table_name} SET {column}={value} WHERE {column} IS NULL;"
            cursor.execute(query, value)
            conn.commit()
        except Exception as e:
            print(f"--Failed to replace NULL values for {column}. Error: {e}.")


def replace(conn, table_name, value, columns=None):
    """
    UPDATE [table]
    SET [column]=0
    WHERE [column] IS NULL;

    PRAGMA table_info(sample_table_1);
    """
    cursor = conn.cursor()
    # if columns:
    #     replace_null_by_column(conn, cursor, table_name, columns, value)
    # else:
    #     query = f"PRAGMA table_info({table_name});"
    #     column_info = cursor.execute(query)
    #     columns = [c[0] for c in column_info]
    #     replace_null_by_column(conn, cursor, table_name, columns, value)
    if columns is None:
        query = f"PRAGMA table_info({table_name});"
        column_info = cursor.execute(query)
        columns = [c[1] for c in column_info]

    replace_null_by_column(conn, cursor, table_name, columns, value)


def get_data_for_desired_columns(conn, table_name, columns):
    if columns is None:
        query = f"SELECT * FROM {table_name}"
    else:
        columns = ",".join(columns)
        query = f"SELECT {columns} from {table_name}"

    cursor = conn.cursor()
    data = cursor.execute(query)
    return list(data)


def get_mean_for_desired_columns(conn, table_name, columns):
    cursor = conn.cursor()
    if columns is None:
        query = f"SELECT AVG(*) FROM {table_name}"
        means = list(cursor.execute(query))
    else:
        means = []
        for column in columns:
            query = f"SELECT AVG({column}) FROM {table_name}"
            m = list(cursor.execute(query))[0][0]
            means.append(m)
    return means


def store_task_result(conn, task_id, result):
    query = """INSERT INTO task_results (task_id, result) VALUES (?, ?)"""
    cursor = conn.cursor()
    cursor.execute(query, [task_id, json.dumps(result)])
    conn.commit()


def get_task_result(conn, task_id):
    query = f"""SELECT result FROM task_results WHERE task_id='{task_id}'"""
    cursor = conn.cursor()
    result = cursor.execute(query)
    result = list(result)
    if not len(result):
        return {
            "task_id": task_id,
            "status": "NOT READY"
        }

    return {
        "task_id": task_id,
        "data": json.loads(result[0][0])
    }


if __name__ == "__main__":
    import os
    dbfile = os.environ.get("DB_FILE")
    conn = connect(dbfile)
    replace(conn, "sample_table_1", "10", columns=["col1"])
    replace(conn, "sample_table_2", "20")
