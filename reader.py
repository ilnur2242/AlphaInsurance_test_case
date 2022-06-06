
import sqlite3
from datetime import date
from sqlite3 import Connection
from rates import Rates
from typing import List


class Reader():
	def __init__(self, conn: Connection) -> None:
		self.__conn = conn


	def get_rates(self, currency:str, start_date: date, end_date: date) -> List[Rates]:
		cursor = self.__conn.cursor()
		query = f'select * from rates where cur="{currency}" and (date between "{start_date.strftime("%Y-%m-%d")}" and "{end_date.strftime("%Y-%m-%d")}")'
		cursor.execute(query)

		rows = cursor.fetchall()
		result: List[Rates] = []
		for row in rows: # check after
			_currency, _value, _date = row
			_date = tuple([int(elem) for elem in _date.split('-')])
			new_rates = Rates(_currency, 'USD', float(_value), date(*_date))
			result.append(new_rates)

		return result