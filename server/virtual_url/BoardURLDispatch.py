import cherrypy


class BoardURLDispatch():


    def __init__(self):
        self.__url_map = {'pepeTest': '99999' }

    @cherrypy.expose
    def default(self,*args,**kwargs):
        return self.__url_map[args[0]]

    @cherrypy.expose
    def index(self,*args,**kwargs):
        raise cherrypy.HTTPRedirect("/")
