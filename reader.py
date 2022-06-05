import imp
import sqlite3
from datetime import date
from sqlite3 import Connection
from rates import Rates
from typing import List


class Reader():
	def __init__(self, conn: Connection) -> None:
		self.__conn = conn


	def get_rates(self, currency:str, start_date: date, end_date: date) -> List[Rates]:
		self.__conn.execute(f'select * from rates where (date between {start_date.strftime("%Y-%m-%d")} and {end_date.strftime("%Y-%m-%d")}) and (cur={currency})')
		rows = self.__conn.fetchall()
		
		result = []
		for row in rows: # check after
			_currency, _value, _date = row.split()
			_date = tuple([int(elem) for elem in _date.split('-')])
			new_rates = Rates(_currency, 'USD', float(_value), date(*_date))
			result.append(new_rates)

		return result