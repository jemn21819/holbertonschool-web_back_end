#!/usr/bin/env python3
"""
0. Regex-ing
"""
from typing import List
import re
import logging
import mysql.connector
from os import getenv
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
     function called filter_datum that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        method to filter values in incoming log records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    function that takes no arguments and returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    function that returns a connector to the database
    (mysql.connector.connection.MySQLConnection object)
    """
    db = mysql.connector.connection.MySQLConnection(
            user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
            password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
            host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
            database=getenv('PERSONAL_DATA_DB_NAME'))
    return db


def main():
    """
    function that takes no arguments and returns nothing.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    for user in users:
        message = f"name={user[0]}; " + \
                  f"email={user[1]}; " + \
                  f"phone={user[2]}; " + \
                  f"ssn={user[3]}; " + \
                  f"password={user[4]}; " + \
                  f"ip={user[5]}; " + \
                  f"last_login={user[6]}; " + \
                  f"user_agent={user[7]};"
        print(message)
        log = logging.LogRecord("my_logger", logging.INFO,
                                None, None, message, None, None)
        formatt = RedactingFormatter(PII_FIELDS)
        formatt.format(log)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
