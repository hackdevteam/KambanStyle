import unittest
import cherrypy
import requests
from server.api.ColumnApiEndPoint import ColumnApiEndPoint
from server.kamban.Url import Url
from server.persistence.PersistenceManager import PersistenceManager
from server.persistence.filesystem.FilesystemPersistence import FilesystemPersistence
from server.test import Commons
from server.test.Commons import remove_data, BASE_FOLDER


class ColumnApiTest(unittest.TestCase):

    def setUp(self):
        remove_data(BASE_FOLDER)
        cherrypy.tree.mount(
            ColumnApiEndPoint(PersistenceManager(FilesystemPersistence(Url(Url.SCHEME_FILE, "localhost", BASE_FOLDER)))), '/api/column',
            {'/':
                 {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
        cherrypy.engine.start()

    def tearDown(self):
        cherrypy.engine.stop()
        cherrypy.engine.exit()
        remove_data(BASE_FOLDER)

    def test_create_column_api_call(self):
        response = requests.post('http://localhost:8080/api/column', {'title': 'Almost more important things',
                                                                      'board_id': Commons.TEST_BOARD_ID})
        self.assertEqual(200, response.status_code)
        self.assertIn('Almost more important things', response.text)


if __name__ == '__main__':
    unittest.main()
