from rates import Rates
from datetime import date
from reader import Reader
from cross_rates import CrossRates
from typing import List
from database import DataBaseConnector

class Task():
	def __init__(self, currency:str,currency_expressed_value:str, start_date: date, end_date: date, path_to_db:str) -> None:
		self._currency = currency
		self._currency_expressed_value = currency_expressed_value
		self._start_date = start_date
		self._end_date = end_date
		self._path_to_db = path_to_db


class TaskPreparer(Task):
	def cross_rates(self,rates_list1: List[Rates], rates_list2: List[Rates])->List[Rates]:
		result : List[Rates] = []
		for rates1 in rates_list1:
			for rates2 in rates_list2:
				if rates1.date == rates2.date:
					cr = CrossRates(rates1,rates2)
					new_rates = cr.get_rates1_by_rates2()
					result.append(new_rates)
					break
		return result


	def check_currency_expressed_value(self):
		conn = DataBaseConnector(self._path_to_db).get_connection()
		db_reader = Reader(conn)
		if self._currency_expressed_value == 'USD':
			rates_list = db_reader.get_rates(
				self._currency, self._start_date, self._end_date)
			return rates_list
		elif self._currency == 'USD':
			rates_list2 = db_reader.get_rates(
				self._currency_expressed_value, self._start_date, self._end_date)
			rates_list = [Rates('USD',self._currency_expressed_value,1/val,date) for val,date in zip([elem.value for elem in rates_list2],[elem.date for elem in rates_list2])]
			return rates_list
		else:
			rates_list1 = db_reader.get_rates(
				self._currency, self._start_date, self._end_date)
			rates_list2 = db_reader.get_rates(
				self._currency_expressed_value, self._start_date, self._end_date)
			rates_list = self.cross_rates(rates_list1,rates_list2)
			return rates_list