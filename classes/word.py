class Word:
  def __init__(self):
    self.characters = ''
    self.type = ''

  def length(self):
    return len(self.characters)

  def setType(self, type):
    self.type = type

  def getType(self):
    return self.type