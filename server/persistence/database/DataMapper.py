from sqlite3 import connect

URL_DATABASE = "C:\\Users\Josue\Desktop\KanbanStyle.sqlite"


class DataMapper:
    def __init__(self):
        self.query = ""

    def launch_query(self, *args):
        connection = connect(URL_DATABASE)
        return connection.execute(self.query, *args)

    def abstract_insert(self, *args):
        #TODO RAM memory access
        self.launch_query(*args)

    def abstract_retrieve(self, *args):
        return self.launch_query(*args)