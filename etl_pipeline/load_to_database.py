import sqlite3

def connect_to_database(etl_pipeline):
    """
    Function to establish a connection to the SQLite database.
    Returns a connection and a cursor.
    """
    conn = sqlite3.connect(etl_pipeline)
    cursor = conn.cursor()
    return conn, cursor


def create_table(cursor):
    """
    Function to create tables in the database.
    You should call this function before loading data into tables.
    """
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS js_posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            body TEXT,
            status TEXT,
            user_id INTEGER
        )
    ''')


def load_data_into_table(cursor, data):
    """
    Function to load transformed data into the appropriate database table.
    :type cursor: object
    """
    try:
        for item in data:
            post_id = item.get('id')
            title = item.get('title')
            body = item.get('body')
            status = item.get('status')
            user = item.get('user', {})
            user_id = user.get('id')

            cursor.execute('''
                INSERT INTO js_posts (id, title, body, status, user_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (post_id, title, body, status, user_id))
    except sqlite3.Error as e:
        print("SQLite error:", e)
