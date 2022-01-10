from data_cleaning_app.repository import get_data_for_desired_columns, get_mean_for_desired_columns


class Aggregator:
    def __init__(self, conn, table_name, columns=None):
        self.conn = conn
        self.table_name = table_name
        self.columns = columns

    def mean(self):
        # data = get_data_for_desired_columns(self.conn, self.table_name, self.columns)
        #
        # # compute mean. TODO: VEEEERY INEFFICIENT. NEEDS REFACTORING. JUST ILLUSTRATES A POINT.
        # # initialize a list with zeros. One value for each column available
        # means = []
        # for _ in data[0]:
        #     means.append(0)
        # # compute mean by adding values one by one to each column
        # for row in data:
        #     for column_index, value in enumerate(row):
        #         means[column_index] = means[column_index] + value
        #
        # for i in range(len(means)):
        #     means[i] = means[i] / len(data)

        means = get_mean_for_desired_columns(self.conn, self.table_name, self.columns)
        return means

