from peewee import Model
from .Database import Database

class BaseModel(Model):
    class Meta:
        database = Database('educationalTexts', 'postgres', '', '0.0.0.0', 5432).getDatabase()
