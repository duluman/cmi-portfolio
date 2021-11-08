import sqlite3

from nightly_workers.reporting.report_builder_base import ReportBuilderBase


class AverageReadingsReportBuilder(ReportBuilderBase):

    chunk = 100

    def __init__(self, producer=None):
        super().__init__()
        self.__conn = None
        self.__producer = producer

    def connect(self):
        self.__conn = sqlite3.connect(self.DATABASE_NAME)

    def __select_chunk_query(self, start_id=0):
        query = f"select id, reading from sensor_data where id > {start_id} and id <= {start_id + self.chunk}"
        return query

    def get_data(self):
        start_id = 0
        data_exists = True
        cur = self.__conn.cursor()
        average_data = {}
        while data_exists:
            statement = self.__select_chunk_query(start_id)
            data = cur.execute(statement)
            if not len(data):
                data_exists = False
            else:
                grouped_data = {}
                for entry in data:
                    if entry[0] in grouped_data.keys():
                        grouped_data[entry[0]].append(entry[1])
                    else:
                        grouped_data[entry[0]] = [entry[1]]

                for key, value in grouped_data.items():
                    if key in average_data.keys():
                        prev_value = average_data[key]['previous_value']
                        n_entries = average_data[key]['previous_entries']
                        average = self.compute_average(prev_value, n_entries, value)
                        average_data[key]['previous_value'] = average
                        average_data[key]['previous_entries'] = n_entries + len(value)
                    else:
                        average = self.compute_average(current_data=value)
                        average_data[key] = {}
                        average_data[key]['previous_value'] = average
                        average_data[key]['previous_entries'] = len(value)
                start_id += self.chunk
        return average_data

    def compute_average(self, prev_value=0, n_entries=0, current_data=None):
        average = (prev_value * n_entries + sum(current_data)) / (n_entries + len(current_data))
        return average

    def compute_report(self):
        try:
            raw_data = self.get_data()
            # process this and save as csv
            message = self.generate_success(filename="average-sensor-reading-report.csv")
        except Exception as e:
            message = self.generate_error(str(e))
        self.__producer.publish(body=message)
