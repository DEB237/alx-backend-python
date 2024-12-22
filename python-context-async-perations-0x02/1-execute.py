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


# Database connection parameters
host = "localhost"
user = "root"  # Replace with MySQL username
password = "password"  # Replace with  MySQL password
database = "ALX_prodev"  # Replace with database name

# Query and parameters
query = "SELECT * FROM users WHERE age > %s"
params = (25,)

# Using the ExecuteQuery context manager
with ExecuteQuery(host, user, password, database, query, params) as executor:
    results = executor.execute()
    for row in results:
        print(row)
