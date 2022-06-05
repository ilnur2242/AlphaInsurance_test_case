from task import Task, TaskPreparer
from datetime import date
from typing import List
from rates import Rates

class ListTask(Task):
	def __init__(self, currency: str, currency_expressed_value: str, start_date: date, end_date: date, path_to_db: str, limit: int) -> None:
		Task.__init__(currency, currency_expressed_value, start_date, end_date, path_to_db)
		self.__limit = limit
		self.__result: List[Rates] = []

	
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