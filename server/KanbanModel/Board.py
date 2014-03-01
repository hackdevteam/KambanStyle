__author__ = 'Ramclen'


class Board():
  def __init__(self, name):
    self.__name = name
    self.__column_dictionary = {}

  def get_name(self):
    return self.__name

  def get_column(self, column_title):
    return self.__column_dictionary[column_title]

  def addColumn(self, column):
    self.__column_dictionary[column.get_title()] = column

  def add_task_to_column(self, column_title, task):
    self.__column_dictionary[column_title].add(task)

  def get_tasks_from_column(self, colunm_title):
    return self.__column_dictionary[colunm_title].get_tasks()

  def remove_task_from_column(self, column_title, task_title):
    self.__column_dictionary[column_title].remove(task_title)