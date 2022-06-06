import sqlite3
from datetime import date
from sqlite3 import Connection
from rates import Rates


class Writer():
	def __init__(self, conn: Connection) -> None:
		self.__conn = conn

	
	def write_new_row(self,rates: Rates):
		cursor = self.__conn.cursor()
		params = [rates.currency,str(rates.value),rates.date.strftime("%Y-%m-%d")]
		cursor.execute('INSERT INTO rates("cur","value","date") VALUES (?,?,?)',params)
		self.__conn.commit()

