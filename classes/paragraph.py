from .Sentence import Sentence

class Paragraph:
  def __init__(self, strParagraph = '', isUnformated = False):
    self.sentences = list()

    if (strParagraph and isUnformated):
      arrSentences = strParagraph.split('.')
      arrSentences = [element for element in arrSentences if element]

      for unformatedSentece in arrSentences:
        sentence = Sentence(unformatedSentece, True)
        self.sentences.append(sentence)

  def addSentece(self, strSentence):
    sentence = Sentence(strSentence)

    self.sentences.push(sentence)

  def join(self, separator):
    paragraph = ''

    for sentence in sentences:
      paragraph = paragraph + sentence.join(separator)

    return paragraph

  def numberOfSentences(self):
    return len(self.sentences)