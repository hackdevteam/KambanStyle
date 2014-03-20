import unittest

import requests
import cherrypy

from server.api.BoardApiEndPoint import BoardApiEndPoint
from server.persistence.filesystem.BoardManager import BoardManager
from server.test import Commons
from server.test.Commons import remove_data, BASE_FOLDER


class BoardApiTest(unittest.TestCase):

    def setUp(self):
        remove_data(BASE_FOLDER)
        cherrypy.tree.mount(
            BoardApiEndPoint(BoardManager(Commons.BASE_FOLDER)), '/api/board',
            {'/':
                 {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
        cherrypy.engine.start()

    def tearDown(self):
        cherrypy.engine.stop()
        cherrypy.engine.exit()
        remove_data(BASE_FOLDER)

    def test_create_board_api_call(self):
        response = requests.post('http://localhost:8080/api/board', params={'name': "Important Things"})
        self.assertEqual(200, response.status_code)
        self.assertIn("Important Things", response.text)


if __name__ == '__main__':
    unittest.main()
