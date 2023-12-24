import sqlite3

def extract_from_sqlite(database_file, table_name):
    """
    Extract data from a SQLite database.

    Parameters:
    - database_file (str): The path to the SQLite database file.
    - table_name (str): The name of the table to extract data from.

    Returns:
    - list: A list of tuples containing the extracted data.
    """

    # Connect to SQLite database
    conn = sqlite3.connect(database_file)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Execute a SELECT query to extract data from the specified table
        query = f"SELECT * FROM {table_name};"

        cursor.execute(query)

        # Fetch the data
        data = cursor.fetchall()

        return data

    except sqlite3.Error as e:
        # Handle any errors that may occur during the extraction
        print(f"Error: {e}")
        return None

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

def get_col_names(database_file, table_name):
    conn = sqlite3.connect(database_file)
    c = conn.cursor()
    c.execute(f"select * from {table_name}")
    return [member[0] for member in c.description]