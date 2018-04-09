from peewee import IntegerField, CharField, DateTimeField, datetime
from .BaseModel import BaseModel

class TextModel(BaseModel):
  '''
    The grade field should have values between [1, 11], where the lowest value represent the first grade in 
    the peruviand education system and the highest the last grade.
  '''
  title = CharField()
  date_created = DateTimeField(default=datetime.datetime.now)
  grade = IntegerField()

  class Meta:
    db_table = 'text'