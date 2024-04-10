import unittest
from unittest.mock import patch, MagicMock
import sys

# Add the directory containing the etl_pipeline package to sys.path
sys.path.insert(1, 'C://Users//DIVYA//PycharmProjects//SDE-Tech-Task-xMpCO//etl_pipeline')

from etl_pipeline import load_to_database

class TestLoadToDatabase(unittest.TestCase):

    @patch('load_to_database.sqlite3.connect')
    def test_load_data_into_table(self, mock_connect):
        # Mock database connection
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = (mock_conn, mock_cursor)

        # Test data
        data = [{'id': 1, 'title': 'Post 1', 'body': 'Body of post 1', 'status': 'lengthy', 'user': {'id': 1}}]

        # Call the function under test
        load_to_database.load_data_into_table(mock_cursor, data)

        # Assertions
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
