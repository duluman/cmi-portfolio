from data_cleaning_app.repository import get_data, delete_data


class DataCleaner:

    def __init__(self, conn, table_name):
        self.__conn = conn
        self.__table_name = table_name

    def remove_duplicates(self, data=None):
        # get data as a list of rows. each row = list of values.
        # [
        #   (1, 199, 204, 'a', 'nsa@sd'),
        #   (2, 199, 204, 'a', 'nsa@sd'),
        #   (3, 199, 204, 'b', 'nsa@sd')
        # ]
        if data is None:
            data = get_data(self.__conn, self.__table_name)
        data_without_ids = [element[1:] for element in data]

        # find duplicated rows
        duplicated_rows = {x for x in data_without_ids if data_without_ids.count(x) > 1}
        for row in duplicated_rows:
            row_ids = [data[idx][0] for idx in range(len(data_without_ids)) if data_without_ids[idx] == row]
            # delete duplicated rows
            for row_id in row_ids[1:]:
                if self.__conn is not None and self.__table_name is not None:
                    delete_data(self.__conn, self.__table_name, column_value=row_id)
                else:
                    print("--Failed to delete row. Missing connection or table_name.")
                    continue

    def remove_rows_with_nulls(self, data=None):
        if data is None:
            data = get_data(self.__conn, self.__table_name)

        # find row ids for rows that contain 'null' or None
        row_ids_with_nulls = [data[i][0] for i in range(len(data)) if None in data[i] or 'null' in data[i]]
        for row_id in row_ids_with_nulls:
            if self.__conn is not None and self.__table_name is not None:
                delete_data(self.__conn, self.__table_name, column_value=row_id)
            else:
                print("--Failed to delete row. Missing connection or table_name.")
                continue


if __name__ == "__main__":
    dc = DataCleaner(None, None)
    data = [
        (1, 199, 204, 'a', 'nsa@sd'),
        (2, 199, 204, 'a', 'nsa@sd'),
        (3, 199, 204, 'b', 'nsa@sd'),
        (4, 199, 204, 'a', 'nsa@sd'),
        (5, 199, 204, 'b', 'nsa@sd'),
        (6, 199, 204, 'null', 'nsa@sd'),
        (7, 199, 204, 'b', 'nsa@sd'),
        (8, 199, None, 'a', 'nsa@sd'),
        (9, None, 204, 'b', 'nsa@sd')
    ]
    # dc.remove_duplicates(data)
    dc.remove_rows_with_nulls(data)