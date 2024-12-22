import mysql.connector

class ExecuteQuery:
    def __init__(self, host, user, password, database, query, params=None):
        """
        Initialize the context manager with database connection parameters,
        the query to execute, and optional parameters for the query.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Establish the database connection and create a cursor.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Database connection established.")
            self.cursor = self.connection.cursor()
            return self
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            raise

    def execute(self):
        """
        Execute the query with the provided parameters.
        """
        if self.cursor:
            self.cursor.execute(self.query, self.params)
            return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the cursor and database connection when exiting the context.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
