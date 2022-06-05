import sqlite3
from datetime import date
from sqlite3 import Connection
from rates import Rates


class Writer():
	def __init__(self, conn: Connection) -> None:
		self.__conn = conn

	
	def write_new_row(self,rates: Rates):
		self.__conn.execute(f'INSERT INTO rates VALUES ({rates.currency},{str(rates.value)},{rates.date.strftime("%Y-%m-%d")})')
		self.__conn.commit()


	def __del__(self):
		self.__conn.close()