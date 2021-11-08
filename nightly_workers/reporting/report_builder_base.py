from datetime import datetime


class ReportBuilderBase:
    DATABASE_NAME = "sensors.db"

    @staticmethod
    def generate_error(error_message):
        message = {
            "error": error_message,
            "timestamp": datetime.utcnow()
        }
        return message

    @staticmethod
    def generate_success(**kwargs):
        message = {
            "timestamp": datetime.utcnow()
        }
        for key, value in kwargs.keys():
            message[key] = value
        return message
