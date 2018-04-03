from peewee import PostgresqlDatabase

class Database:
  def __init__(self, databaseName, user, password, host, port):
    self.database = PostgresqlDatabase(databaseName, user=user, password=password, host=host, port=port)

  def getDatabase(self):
    return self.database

  def establishConnection(self):
    self.database.connect()

  def closeConnetion(self):
    self.database.close()

  def createTables(self, arrOfTables):
    with self.database:
      print(self.database)
      self.database.create_tables(arrOfTables)