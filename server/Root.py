import os

import cherrypy
from server.api.ColumnApiEndPoint import ColumnApiEndPoint
from server.api.TaskApiEndPoint import TaskApiEndPoint

from server.api.BoardApiEndPoint import BoardApiEndPoint
from server.kamban.Url import Url
from server.persistence.PersistenceManager import PersistenceManager
from server.persistence.filesystem.FilesystemPersistence import FilesystemPersistence

API_BOARD = '/api/my_board'
API_COLUMN = '/api/column'
API_TASK = '/api/task'


class Root():
    def __init__(self):
        self.__config = ""
        self.__persistence = PersistenceManager(FilesystemPersistence(Url(Url.SCHEME_FILE, "localhost", "filesystem_database")))
        self.config_server_to_serve_static_content()
        self.mount_end_point(BoardApiEndPoint(self.__persistence), API_BOARD)
        self.mount_end_point(ColumnApiEndPoint(self.__persistence), API_COLUMN)
        self.mount_end_point(TaskApiEndPoint(self.__persistence), API_TASK)
        self.start_server()

    def config_server_to_serve_static_content(self):
        self.__config = {'/': {'tools.staticdir.on': True,
                               'tools.staticdir.dir': os.path.abspath("../client/"),
                               'tools.staticdir.index': 'index.html'}}

    def mount_end_point(self, end_point,end_point_uri):
        cherrypy.tree.mount(end_point,
                            end_point_uri,
                            {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})

    def start_server(self):
        cherrypy.quickstart(self, config=self.__config)


if __name__ == '__main__':
    Root()