from tasks.task import Task, TaskPreparer
from datetime import date
from typing import List
from rates import Rates

class ListTask(Task):
	def __init__(self, currency: str, currency_expressed_value: str, start_date: date, end_date: date, path_to_db: str, limit: int) -> None:
		self._currency = currency
		self._currency_expressed_value = currency_expressed_value
		self._start_date = start_date
		self._end_date = end_date
		self._path_to_db = path_to_db
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
			self._end_date,
			self._path_to_db)

		rates_list = tp.check_currency_expressed_value()

		i=0
		while i < len(rates_list) and i < self.__limit:
			self.__result.append(rates_list[i])
			i+=1
		return self.result

	
	def __str__(self):
		self_result_len = len(self.result)
		Count = self.__limit if self.__limit < self_result_len else self_result_len
		return 'Count = {}\n'.format(Count) + '\n'.join([f'{i+1}. {val.value}' for i, val in enumerate(self.result)])