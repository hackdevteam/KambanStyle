class Column():
  def __init__(self, title):
    self.__title = title
    self.task_dictionary = {}

  def get_title(self):
    return self.__title

  def add(self, task):
    self.task_dictionary[task.get_title()] = task

  def get_task(self, task_title):
    return self.task_dictionary[task_title.get_title()]

  def get_tasks(self):
    return self.task_dictionary

  def remove(self, task_title):
    self.task_dictionary.__delitem__(task_title)