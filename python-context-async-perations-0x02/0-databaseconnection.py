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


# Database connection parameters
host = "localhost"
user = "root"  # Replace with your MySQL username
password = "password"  # Replace with your MySQL password
database = "ALX_prodev"  # Replace with your database name

# Query and parameters
query = "SELECT * FROM users WHERE age > %s"
params = (25,)

# Using the ExecuteQuery context manager
with ExecuteQuery(host, user, password, database, query, params) as executor:
    results = executor.execute()
    for row in results:
        print(row)