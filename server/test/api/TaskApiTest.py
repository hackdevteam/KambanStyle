import unittest
import cherrypy
import requests
from server.api.TaskApiEndPoint import TaskApiEndPoint
from server.persistence.filesystem.BoardManager import BoardManager
from server.test import Commons


class TaskApiTest(unittest.TestCase):
    def setUp(self):
        cherrypy.tree.mount(
            TaskApiEndPoint(BoardManager(Commons.BASE_FOLDER)), '/api/task',
            {'/':
                 {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
        cherrypy.engine.start()

    def tearDown(self):
        cherrypy.engine.stop()
        cherrypy.engine.exit()

    def test_create_task(self):
        response = requests.post('http://localhost:8080/api/task',
                                 {'title': 'Thing to do',
                                  'description': 'Important thing to do',
                                  'column_id': Commons.TEST_BOARD_COLUMN_ID})
        self.assertEqual(200, response.status_code)
        self.assertIn('Thing to do', response.text)


if __name__ == '__main__':
    unittest.main()
