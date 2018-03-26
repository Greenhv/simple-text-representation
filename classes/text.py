from .Paragraph import Paragraph
from .Sentence import Sentence

class Text:
  def __init__(self):
    self.paragraphs = list()
    self.unformatedParagraphs = list()
    self.title = ''

  def toString(self):
    text = ''

    for paragraph in paragraphs:
      text = text + paragraph.join(' ') + '\n'
    
    return text

  def setTitle(self, title):
    self.title = title

  def getTitle(self):
      return self.title

  def addParagraph(self, paragrah):
    return self.paragraphs.append(paragrah)

  def setUnformatedParagraphs(self, unformatedParagraphs):
    self.unformatedParagraphs = unformatedParagraphs

  def formatParagraphs(self):
    for uParagraph in self.unformatedParagraphs:
      for unformatedParagraph in uParagraph:
        paragraph = Paragraph(unformatedParagraph, True)
        self.paragraphs.append(paragraph)