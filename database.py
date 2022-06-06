from operator import imod
import sqlite3
from sqlite3 import Connection
from sqlite3 import Error
# pattern repositiry
# как оформить работа базы данных в питоне; версионность бд
class DataBaseConnector():
	def __init__(self,path):
		self.__path = path


	def create_data_base(self):
		self.conn = None
		try:
			self.conn = sqlite3.connect(self.__path)
			query = '''CREATE TABLE rates(
					cur VARCHAR(10),
					value FLOAT,
					date DATE);'''
			cursor =  self.conn.cursor()
			cursor.execute(query)
			self.conn.commit()
		except Error as e:
			print(e)
			self.conn = sqlite3.connect(self.__path)
		return self.conn

	def get_connection(self)->Connection:
		self.conn = None
		try:
			self.conn = sqlite3.connect(self.__path)
			return self.conn
		except Error as e:
			print(e)



	

		
		




		

