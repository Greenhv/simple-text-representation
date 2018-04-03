class Word:
  def __init__(self, strWord):
    self.characters = ''
    self.type = ''

    if (strWord):
      word = self.removeSpecialCharacters(strWord)
      self.characters = word

  def removeSpecialCharacters(self, strWord):
    return ''.join(character for character in strWord if character.isalnum())

  def getChars(self):
    return self.characters

  def length(self):
    return len(self.characters)

  def setType(self, type):
    self.type = type

  def getType(self):
    return self.type