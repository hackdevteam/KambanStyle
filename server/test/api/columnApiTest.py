import unittest

import cherrypy
import requests

from server.api.ColumnApiTest import ColumnApiEndPoint
from server.test.api.BoardApiTest import PersistenceMock


class ColumnApiTest(unittest.TestCase):

    def setUp(self):
        cherrypy.tree.mount(
            ColumnApiEndPoint(PersistenceMock()), '/api/column',
            {'/':
                 {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
        cherrypy.engine.start()

    def tearDown(self):
        cherrypy.engine.stop()
        cherrypy.engine.exit()

    def test_create_column_api_call(self):
        response = requests.post('http://localhost:8080/api/column', {'name': 'Almost more important things'})
        self.assertEqual(200, response.status_code)
        self.assertIn('Almost more important things', response.text)


if __name__ == '__main__':
    unittest.main()
