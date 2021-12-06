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
    