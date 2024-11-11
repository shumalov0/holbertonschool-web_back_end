#!/usr/bin/env python3
'''Filtered logger'''
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''Filtering values of the required fields'''
    for item in fields:
        message = re.sub(f"{item}=.*?{separator}",
                         f"{item}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Formatting methodj'''
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    '''get logger()'''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(stream)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Get connector to database'''
    mydb = mysql.connector.connect(
        host=os.environ["PERSONAL_DATA_DB_HOST"],
        user=os.environ["PERSONAL_DATA_DB_USERNAME"],
        password=os.environ['PERSONAL_DATA_DB_PASSWORD'],
        database=os.environ["PERSONAL_DATA_DB_NAME"]
    )
    return mydb


def main() -> None:
    '''Main method'''
    connector = get_db()

    cursor = connector.cursor()
    cursor.execute("SELECT * FROM users")

    data = cursor.fetchall()

    logger = get_logger()

    for line in data:
        logger.info(line)

    cursor.close()
    connector.close()


if __name__ == "__main__":
    main()
