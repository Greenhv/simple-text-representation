from .Sentence import Sentence
from ..models.ParagraphModel import ParagraphModel

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

    for sentence in self.sentences:
      paragraph = paragraph + sentence.join(separator)

    return paragraph

  def save(self, database, textId):
    try:
      with database.getDatabase().transaction():
        paragraph = ParagraphModel.create(
          text=textId
        )
        for sentence in self.sentences:
          sentence.save(database, paragraph.id)
    except IntegrityError:
      print('Somethinig went wrong!')


  def numberOfSentences(self):
    return len(self.sentences)