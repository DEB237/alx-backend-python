import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        """
        Initialize with database connection parameters.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        """
        Establish the database connection when entering the context.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Database connection established.")
            return self.connection
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the database connection when exiting the context.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")

