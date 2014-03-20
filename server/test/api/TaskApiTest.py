import unittest

import cherrypy
import requests

from server.api.TaskApiEndPoint import TaskApiEndPoint
from server.kamban.model.Column import Column
from server.persistence.filesystem.BoardManager import BoardManager
from server.test import Commons
from server.test.Commons import remove_data, BASE_FOLDER


class TaskApiTest(unittest.TestCase):
    def setUp(self):
        remove_data(BASE_FOLDER)
        cherrypy.tree.mount(
            TaskApiEndPoint(BoardManager(Commons.BASE_FOLDER)), '/api/task',
            {'/':
                 {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
        cherrypy.engine.start()
        self.column = Column("a column", Commons.TEST_BOARD_ID)
        BoardManager(BASE_FOLDER).save_column(self.column)

    def tearDown(self):
        cherrypy.engine.stop()
        cherrypy.engine.exit()
        remove_data(BASE_FOLDER)

    def test_create_task(self):
        response = requests.post('http://localhost:8080/api/task',
                                 {'title': 'Thing to do',
                                  'description': 'Important thing to do',
                                  'column_id': self.column.get_id()})
        self.assertEqual(200, response.status_code)
        self.assertIn('Thing to do', response.text)


if __name__ == '__main__':
    unittest.main()
