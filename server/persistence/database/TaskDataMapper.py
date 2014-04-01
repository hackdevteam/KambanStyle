from server.persistence.database.DataMapper import DataMapper


class TaskDataMapper(DataMapper):
    def __init__(self):
        super.__init__()

    def insert(self, task):
        super.query = "INSERT INTO task (title, description, idc) VALUES(?,?,?)"
        super.abstract_insert((task.get_title(), task.get_description(), task.get_column_id()))


