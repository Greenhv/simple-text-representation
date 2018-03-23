from .sentence import Sentence

class Paragrah:
  def __init__(self):
    self.sentences = list()

  def addSentece(self, strSentence):
    sentence = Sentence(strSentence)

    self.sentences.push(sentence)

  def join(self, separator):
    paragrah = ''

    for sentence in sentences:
      paragrah = paragrah + sentence.join(separator)

    return paragrah

  def numberOfSentences(self):
    return len(self.sentences)