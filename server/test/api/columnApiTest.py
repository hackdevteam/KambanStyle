import unittest
import requests




class ColumnApiTest(unittest.TestCase):
    def test_create_column_api_call(self):
        response = requests.post('http://localhost:8080/api/board/1/column', {'name': 'Almost more important things'})
        self.assertEqual(200, response.status_code)
        self.assertIn('Almost more important things', response.text)


if __name__ == '__main__':
    unittest.main()
