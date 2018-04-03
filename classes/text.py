from .Paragraph import Paragraph
from ..models.TextModel import TextModel

class Text:
  def __init__(self):
    self.paragraphs = list()
    self.unformatedParagraphs = list()
    self._title = ''

  def toString(self):
    text = ''

    for paragraph in self.paragraphs:
      text = text + paragraph.join(' ') + '\n'

    return text

  def setTitle(self, newTitle):
    self._title = newTitle

  def getTitle(self):
      return self._title

  def addParagraph(self, paragrah):
    return self.paragraphs.append(paragrah)

  def setUnformatedParagraphs(self, unformatedParagraphs):
    self.unformatedParagraphs = unformatedParagraphs

  def formatParagraphs(self):
    for uParagraph in self.unformatedParagraphs:
      paragraph = Paragraph(uParagraph, True)
      self.paragraphs.append(paragraph)

  def save(self, database):
    try:
      database.establishConnection()

      with database.getDatabase().transaction():
        text = TextModel.create(
          title=self._title
        )
        for paragraph in self.paragraphs:
          paragraph.save(database, text.id)
      database.closeConnetion()
    except IntegrityError:
      print('Somethinig went wrong!')


