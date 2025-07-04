import psycopg
from psycopg.rows import dict_row
import os

# This class helps us interact with the database, wrapping the underlying psycopg library

class DatabaseConnection:
    DATABASE_NAME = "social_network"

    # Connect to Postgres using the psycopg library. 
    # Connect to localhost and select the database name given in argument.

    def connect(self):
        try:
            self.connection = psycopg.connect(
                f"postgresql://localhost/{self.DATABASE_NAME}",
                row_factory=dict_row)
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database {self.DATABASE_NAME}! " \
                    f"Did you create it using `createdb {self.DATABASE_NAME}`?")

    # Seed the database with the given SQL file.
    # Set up the database ready for our tests or application.

    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    # Execute an SQL query on the database.
    # It allows you to set some parameters too

    def execute(self, query, params=[]):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = '' \
        'DatabaseConnection.exec_params: Cannot run a SQL query as ' \
        'the connection to the database was never opened. Did you ' \
        'make sure to call first the method DatabaseConnection.connect` ' \
        'in your app.py file (or in your tests)?'

    # Private method to check that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)
