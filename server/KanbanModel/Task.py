
class Task():
  def __init__(self, title, description):
    self.__title = title
    self.__description = description

  def get_title(self):
    return self.__title

  def get_description(self):
    return self.__description