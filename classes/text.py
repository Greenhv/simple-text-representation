from .Paragraph import Paragraph
from ..models.TextModel import TextModel

class Text:
  def __init__(self):
    self.paragraphs = list()
    self.unformatedParagraphs = list()
    self.title = ''
    self.grade = -1

  def toString(self):
    text = ''

    for paragraph in self.paragraphs:
      text = text + paragraph.join(' ') + '\n'

    return text

  def setGrade(self, grade):
    self.grade = grade
  
  def getGrade(self):
    return self.grade

  def setTitle(self, newTitle):
    self.title = newTitle

  def getTitle(self):
      return self.title

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
          title=self.title
          grade=self.grade
        )
        for paragraph in self.paragraphs:
          paragraph.save(database, text.id)
      database.closeConnetion()
    except IntegrityError:
      print('Somethinig went wrong!')


