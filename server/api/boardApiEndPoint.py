import cherrypy
from server.KanbanModel.Board import Board

boards = {'1': "default"}


class BoardApiEndPoint(object):
    exposed = True

    def POST(self, name):
        board = Board(name)
        identification = str(max([int(_) for _ in boards.keys()]) + 1)
        boards[identification] = board.get_name()
        return {boards[identification]}

if __name__ == '__main__':
    cherrypy.tree.mount(
        BoardApiEndPoint(), '/api/board',
        {'/':
             {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()