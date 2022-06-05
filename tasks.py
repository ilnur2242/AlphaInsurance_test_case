from rates import Rates
from datetime import date
from reader import Reader
from cross_rates import CrossRates
from typing import List

class Task():
	def __init__(self, currency:str,currency_expressed_value:str, start_date: date, end_date: date) -> None:
		self._currency = currency
		self._currency_expressed_value = currency_expressed_value
		self._start_date = start_date
		self._end_date = end_date


class TaskPreparer(Task):
	def cross_rates(self,rates_list1: List[Rates], rates_list2: List[Rates])->List[Rates]:
		result = []
		for rates1, rates2 in zip(rates_list1,rates_list2): # !!!!
			cr = CrossRates(rates1,rates2)
			new_rates = cr.get_rates1_by_rates2()
			result.append(new_rates)
		return result


	def check_currency_expressed_value(self):
		db_reader = Reader()
		if self._currency_expressed_value == 'USD':
			rates_list = db_reader.get_rates(
				self._currency, self._start_date, self._end_date)
			return rates_list
		else:
			rates_list1 = db_reader.get_rates(
				self._currency, self._start_date, self._end_date)
			rates_list2 = db_reader.get_rates(
				self._currency_expressed_value, self._start_date, self._end_date)
			rates_list = self.cross_rates(rates_list1,rates_list2)
			return rates_list
			

class MinMaxTask(Task):
	def __init__(self, currency: str, currency_expressed_value: str, start_date: date, end_date: date) -> None:
		Task.__init__(currency, currency_expressed_value, start_date, end_date)
		self.__min_val = 0
		self.__max_val = 0


	@property
	def min_val(self):
		return self.__min_val


	@property
	def max_val(self):
		return self.__max_val


	def get_minmax_values(self):
		tp = TaskPreparer(
			self._currency,
			self._currency_expressed_value,
			self._start_date,
			self._end_date)

		rates_list = tp.check_currency_expressed_value()
		rates_list.sort(key=lambda x: x.value)

		self.__min_val = rates_list[-1].value
		self.__max_val = rates_list[0].value

		return (self.__min_val, self.__max_val)

	def __str__(self):
		return 'MIN = {}\nMAX = {}'.format(self.min_val, self.max_val)



		

class ListTask(Task):
	def __init__(self, currency: str, currency_expressed_value: str, start_date: date, end_date: date, limit: int) -> None:
		Task.__init__(currency, currency_expressed_value, start_date, end_date)
		self.__limit = limit
		self.__result = []

	
	@property
	def result(self):
		return self.__result


	def get_limited(self):
		tp = TaskPreparer(
			self._currency,
			self._currency_expressed_value,
			self._start_date,
			self._end_date)

		rates_list = tp.check_currency_expressed_value()

		i=0
		while i < len(rates_list) or i < self.__limit:
			self.__result.append(rates_list[i])
			i+=1
		return self.result

	
	def __str__(self):
		return 'Count = {}\n'.format(self.__limit) + '\n'.join([f'{i+1}. {val.value}' for i, val in enumerate(self.result)])



		

	
