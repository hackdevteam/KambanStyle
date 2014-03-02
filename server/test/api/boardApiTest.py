import unittest
from urllib import request


class BoardApiTest(unittest.TestCase):

    def test_create_board_api_call(self):
        response = request.post('localhost/api/board', params={'name': "Important Things"})
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
