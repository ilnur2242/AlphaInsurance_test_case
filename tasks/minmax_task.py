from tasks.task import Task, TaskPreparer
from datetime import date
from rates import Rates

class MinMaxTask(Task):
	""" def __init__(self, currency: str, currency_expressed_value: str, start_date: date, end_date: date, path_to_db: str) -> None:
		Task.__init__(currency, currency_expressed_value, start_date, end_date, path_to_db)
		self.__min_val = 0
		self.__max_val = 0 """


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
			self._end_date,
			self._path_to_db)

		rates_list = tp.check_currency_expressed_value()
		rates_list.sort(key=lambda x: x.value)

		self.__min_val = rates_list[0].value
		self.__max_val = rates_list[-1].value

		return (self.__min_val, self.__max_val)

	def __str__(self):
		return 'MIN = {}\nMAX = {}'.format(self.min_val, self.max_val)