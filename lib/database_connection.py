import psycopg
import os

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            # For psycopg3, use 'dbname' instead of 'database'
            self.connection = psycopg.connect(
                host="127.0.0.1",
                dbname="finance_tracker",  # Changed from 'database' to 'dbname'
                user=os.environ.get("POSTGRES_USER", ""),
                password=os.environ.get("POSTGRES_PASSWORD", "")
            )
        except psycopg.OperationalError as e:
            raise Exception(f"Couldn't connect to the database! " +
                          f"Did you create the database finance_tracker? Error: {e}")

    def seed(self, sql_filename):
        self._check_connection()
        if sql_filename != "":
            sql_string = self._read_sql_file(sql_filename)
            with self.connection.cursor() as cursor:
                cursor.execute(sql_string)
                self.connection.commit()

    def execute(self, query, params=None):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                return cursor.fetchall()
            else:
                return None

    def _check_connection(self):
        if self.connection is None:
            raise Exception("DatabaseConnection.connect() must be called first")

    def _read_sql_file(self, filename):
        with open(filename, "r") as file:
            return file.read()