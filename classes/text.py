from .paragraph import Paragrah

class Text:
  def __init__(self):
    self.paragraphs = list()

  def toString(self):
    text = ''

    for paragraph in paragraphs:
      text = text + paragraph.join(' ') + '\n'
