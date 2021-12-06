from data_cleaning_app.repository import get_data, delete_data


class DataCleaner:

    def __init__(self, conn, table_name):
        self.__conn = conn
        self.__table_name = table_name

    def remove_duplicates(self):
        # get data as a list of rows. each row = list of values.
        # [
        #   [1, 199, 204, 'a', 'nsa@sd'],
        #   [2, 199, 204, 'a', 'nsa@sd'],
        #   [3, 199, 204, 'b', 'nsa@sd']
        # ]
        data = get_data(self.__conn, self.__table_name)
        # find duplicated rows
        # duplicated_data_row_ids = [2]
        duplicated_data_row_ids = []

        # delete duplicated rows
        for row_id in duplicated_data_row_ids:
            delete_data(self.__conn, self.__table_name, column_value=row_id)
