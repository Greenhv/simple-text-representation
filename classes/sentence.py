from .Word import Word

class Sentence:
  def __init__(self, strSentence = '', isUnformated = False):
    self.words = list()

    if (strSentence and isUnformated):
      arrWords = strSentence.split(' ')
      for wordIter in arrWords:
        word = Word(wordIter)

  def join(self, separator):
    return separator.join(self.words) + '.'

  def numberOfWord(self):
    return len(self.words)