import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import pool

# Load environment variables
load_dotenv()

# Retrieve database credentials
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Initialize a connection pool
try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        minconn=1,  # Minimum number of connections
        maxconn=10,  # Maximum number of connections
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    if connection_pool:
        print("Connection pool created successfully")
except Exception as e:
    print(f"Error creating connection pool: {e}")
    connection_pool = None


def get_db_connection():
    """
    Retrieve a connection from the connection pool.
    """
    try:
        connection = connection_pool.getconn()
        return connection
    except Exception as e:
        print(f"Error getting connection: {e}")
        return None


def release_db_connection(connection):
    """
    Return the connection to the pool.
    """
    try:
        if connection:
            connection_pool.putconn(connection)
    except Exception as e:
        print(f"Error releasing connection: {e}")


def close_all_connections():
    """
    Close all connections in the pool.
    """
    try:
        connection_pool.closeall()
        print("All connections closed")
    except Exception as e:
        print(f"Error closing connections: {e}")


def execute_query(query, params=None):
    """
    Execute a query and return results.
    :param query: The SQL query to execute.
    :param params: The parameters for the query (default: None).
    :return: The query results or None if an error occurs.
    """
    connection = get_db_connection()
    if not connection:
        print("Failed to get database connection.")
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        results = cursor.fetchall()  # Use fetchone() for a single result
        return results
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        release_db_connection(connection)


def insert_query(query, params=None):
    """
    Execute a query and return results.
    :param query: The SQL query to execute.
    :param params: The parameters for the query (default: None).
    :return: The query results or None if an error occurs.
    """
    connection = get_db_connection()
    if not connection:
        print("Failed to get database connection.")
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        connection.commit()
        return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
        return False
    finally:
        release_db_connection(connection)


def insert_multiple_query(querys):
    """
    Execute a query and return results.
    :param query: The SQL query to execute.
    :param params: The parameters for the query (default: None).
    :return: The query results or None if an error occurs.
    """
    connection = get_db_connection()
    if not connection:
        print("Failed to get database connection.")
        return None

    try:
        cursor = connection.cursor()
        # Insert sentences and their embeddings into the PostgreSQL database
        for i, query in enumerate(querys):
            # Insert into the table
            cursor.execute(query)
        connection.commit()
        return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
        return False
    finally:
        release_db_connection(connection)
