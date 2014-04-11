import cherrypy


class BoardURLDispatch():
    def __init__(self):
        self.__url_map = {'pepeTest': '99999'}

    @cherrypy.expose
    def default(self, *args, **kwargs):
        return self.load_URL(args[0])

    @cherrypy.expose
    def index(self, *args, **kwargs):
        raise cherrypy.HTTPRedirect("/")

    def load_URL(self, param):
        if param in self.__url_map.keys():
            return self.__url_map[param]
        else:
            raise cherrypy.HTTPError("404 URL not found", "Check out your URL\n we can not find")


