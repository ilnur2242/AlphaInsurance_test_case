from operator import imod
import sqlite3
from sqlite3 import Connection
from sqlite3 import Error
# pattern repositiry
# как оформить работа базы данных в питоне; версионность бд
class DataBaseConnector():
	def __init__(self,path):
		self.__path = path

	def __create_data_base(self):
		pass


	def get_connection(self)->Connection:
		conn = None
		try:
			conn = sqlite3.connect(self.__path)
			return conn
		except Error as e:
			print(e)
		finally:
			exit(1)

		
		




		

