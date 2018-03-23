from .word import Word

class Sentence:
  def __init__(self, strSentence):
    self.words = list()

  def join(self, separator):
    separator.join(self.words)

  def numberOfWord(self):
    return len(self.words)