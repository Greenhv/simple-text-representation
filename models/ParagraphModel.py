from peewee import ForeignKeyField, DateTimeField, datetime

from .BaseModel import BaseModel
from .TextModel import TextModel

class ParagraphModel(BaseModel):
  text = ForeignKeyField(TextModel, backref='paragraphs')
  date_created = DateTimeField(default=datetime.datetime.now)

  class Meta:
    db_table = 'paragraph'