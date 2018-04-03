from peewee import TextField, ForeignKeyField, DateTimeField, datetime

from .BaseModel import BaseModel
from .ParagraphModel import ParagraphModel

class SentenceModel(BaseModel):
  paragraph = ForeignKeyField(ParagraphModel, backref='sentences')
  value = TextField()
  date_created = DateTimeField(default=datetime.datetime.now)

  class Meta:
    db_table = 'sentence'