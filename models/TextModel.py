from peewee import CharField, DateTimeField, datetime
from .BaseModel import BaseModel

class TextModel(BaseModel):
  title = CharField()
  date_created = DateTimeField(default=datetime.datetime.now)

  class Meta:
    db_table = 'text'