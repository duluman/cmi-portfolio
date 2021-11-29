import sqlite3


def connect(dbfile):
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Exception as e:
        print(f"--Failed to connect to the database {dbfile}. Error: {e}.")
        return None


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


def insert_data(conn, data, table_name, columns):
    """
    1) INSERT INTO {table_name} (col1, col2, ...) VALUES (?, ?, ...)
    columns = {
        column_name: column_type
    }
    data = pandas.DataFrame()
    """
    # generate query to insert data (1)

    # get cursor

    # run query
    # cursor.execute(query, data)

    # commit changes
    # conn.commit()
