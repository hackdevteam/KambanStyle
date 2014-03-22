import unittest

import requests
import cherrypy

from server.api.BoardApiEndPoint import BoardApiEndPoint

from server.kamban.Url import Url
from server.persistence.PersistenceManager import PersistenceManager
from server.persistence.filesystem.FilesystemPersistence import FilesystemPersistence
from server.test.Commons import remove_data, BASE_FOLDER


class BoardApiTest(unittest.TestCase):
    def setUp(self):
        remove_data(BASE_FOLDER)
        cherrypy.tree.mount(
            BoardApiEndPoint(PersistenceManager(FilesystemPersistence(Url(Url.SCHEME_FILE, "localhost", BASE_FOLDER)))),
            '/api/board',
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
