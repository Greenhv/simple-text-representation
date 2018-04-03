from .Word import Word
from ..models.SentenceModel import SentenceModel

class Sentence:
  def __init__(self, strSentence = '', isUnformated = False):
    self.words = list()

    if (strSentence and isUnformated):
      arrWords = strSentence.split(' ')
      for wordIter in arrWords:
        word = Word(wordIter)
        self.words.append(word)

  def join(self, separator):
    sentence = ''

    for index, word in enumerate(self.words):
      sentence = sentence + word.getChars()
      sentence = sentence + (separator if index < len(self.words) - 1 else '')

    return sentence + '.'

  def save(self, database, paragraphId):
    try:
      with database.getDatabase().transaction():
        sentence = SentenceModel.create(
          paragraph=paragraphId,
          value=self.join(' ')
        )
    except IntegrityError:
      print('Somethinig went wrong!')

  def numberOfWord(self):
    return len(self.words)