# Put your unit tests here
import unittest
from unittest.mock import patch
import sys
sys.path.insert(1, 'C://Users//DIVYA//PycharmProjects//SDE-Tech-Task-xMpCO//etl_pipeline')
from etl_pipeline import api_client

class TestAPIClient(unittest.TestCase):

    @patch('api_client.requests.get')
    def test_get_posts(self, mock_get):
        # Mock API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'id': 1, 'title': 'Post 1', 'body': 'Body of post 1'}]

        # Call the function under test
        posts = api_client.get_posts()

        # Assertions
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['id'], 1)
        self.assertEqual(posts[0]['title'], 'Post 1')
        self.assertEqual(posts[0]['body'], 'Body of post 1')


if __name__ == '__main__':
    unittest.main()
