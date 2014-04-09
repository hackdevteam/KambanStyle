import unittest
import cherrypy
import requests
from server.Root import Root
from server.virtual_url.BoardURLDispatch import BoardURLDispatch


class BoardURLDispatchTest(unittest.TestCase):
    def setUp(self):
        cherrypy.tree.mount(
            BoardURLDispatch(),
            '/url'
        )
        cherrypy.engine.start()

    def tearDown(self):
        cherrypy.engine.stop()
        cherrypy.engine.exit()

    def test_boardURLDispatch_responds(self):
        response = requests.post('http://localhost:8080/url/pepeTest')
        self.assertEqual(200, response.status_code)

    def test_board_id_load(self):
        response = requests.post('http://localhost:8080/url/pepeTest')
        self.assertEqual(200, response.status_code)
        self.assertEqual('99999', response.text)
        
if __name__ == '__main__':
    unittest.main()
