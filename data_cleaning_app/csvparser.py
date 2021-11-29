import pandas as pd
from io import StringIO


class CsvParser:
    __DEFAULT_COLUMN_TYPE = 'TEXT'

    __PANDAS_TO_SQLITE_TYPE_MAPPER = {
        'object': 'TEXT',
        'int64': 'INTEGER',
        'float64': 'REAL',
        'bool': 'INTEGER',
        'timedelta[ns]': 'INTEGER'
    }

    def __init__(self, data_string=None):
        self.data_string = data_string
        self.dataframe = None
        self.data_columns = None
        self.data_columns_type = {}

    def to_dataframe(self):
        if self.data_string is None:
            print("--Failed to convert string to dataframe. Missing data string.")
            raise Exception("Missing data string.")

        data = StringIO(self.data_string)
        self.dataframe = pd.read_csv(data, sep=",")
        return self

    def get_columns(self):
        if self.dataframe is None:
            print("--Failed to extract columns. Missing dataframe.")
            raise Exception("Missing dataframe.")

        self.data_columns = list(self.dataframe.columns)
        return self

    def get_column_types(self):
        if self.data_columns is None:
            print("--Failed to extract columns type. Missing data columns.")
            raise Exception("Missing data columns.")

        for column in self.data_columns:
            column_type = str(self.dataframe.dtypes[column])
            if column_type in self.__PANDAS_TO_SQLITE_TYPE_MAPPER.keys():
                self.data_columns_type[column] = self.__PANDAS_TO_SQLITE_TYPE_MAPPER[column_type]
            else:
                self.data_columns_type[column] = self.__DEFAULT_COLUMN_TYPE

        return self.data_columns_type

    def convert_dataframe_to_sqlite_data(self):
        data = []
        for row in self.dataframe.iterrows():
            converted_row = []
            for key in self.data_columns:
                if pd.isna(row[1][key]):
                    converted_row.append(None)
                elif self.data_columns_type[key] == 'INTEGER':
                    converted_row.append(int(row[1][key]))
                elif self.data_columns_type[key] == 'TEXT' and type(row[1][key]) == str:
                    converted_row.append(row[1][key])
                elif self.data_columns_type[key] == 'TEXT' and type(row[1][key]) != str:
                    converted_row.append(str(row[1][key]))
                elif self.data_columns_type[key] == 'REAL':
                    converted_row.append(float(row[1][key]))

            data.append(converted_row)
        return data


if __name__ == "__main__":
    sample_csv = """col1,col2,col3,col4
    1,4.4,99,True
    2,,200,False
    3,4.7,'65',True
    4,3.2,'st',True
    """

    parser = CsvParser(sample_csv)

    column_types = parser.to_dataframe().get_columns().get_column_types()
    print(column_types)

    data = parser.convert_dataframe_to_sqlite_data()
    print(data)
