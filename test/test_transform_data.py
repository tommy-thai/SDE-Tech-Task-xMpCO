# Put your unit tests here
import unittest
from unittest.mock import patch
from etl_pipeline import transform_data

class TestTransformData(unittest.TestCase):

    def test_parse_embedded_json(self):
        # Test data with embedded JSON
        data = [{'id': 1, 'title': 'Post 1', 'body': '{"embedded_key": "value"}'}]

        # Call the function under test
        transformed_data = transform_data.parse_embedded_json(data)

        # Assertions
        self.assertEqual(transformed_data[0]['body'], {"embedded_key": "value"})

    def test_add_computed_status(self):
        # Test data with different body lengths
        data = [{'id': 1, 'title': 'Post 1', 'body': 'Short body'},
                {'id': 2, 'title': 'Post 2', 'body': 'Long body exceeding 100 characters' * 5}]

        # Call the function under test
        transformed_data = transform_data.add_computed_status(data)

        # Assertions
        self.assertEqual(transformed_data[0]['status'], 'concise')
        self.assertEqual(transformed_data[1]['status'], 'lengthy')

if __name__ == '_main_':
    unittest.main()
