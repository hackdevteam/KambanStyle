import unittest
import requests


class BoardApiTest(unittest.TestCase):

    def test_create_board_api_call(self):
        response = requests.post('http://localhost:8080/api/board', params={'name': "Important Things"})
        self.assertEqual(200, response.status_code)
        self.assertIn("Important Things", response.text)


if __name__ == '__main__':
    unittest.main()
