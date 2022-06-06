from tasks.minmax_task import MinMaxTask
from tasks.list_task import ListTask
import click
from datetime import date


class CosoleApplication():
	def __init__(self, path_to_db: str, mode: str, currency: str, start_date: date, end_date: date, option: int, currency_expressed_value='USD') -> None:
		self.path_to_db = path_to_db
		self.__mode = mode
		self.__currency = currency
		self.__currency_expressed_value = currency_expressed_value
		self.__start_date = start_date
		self.__end_date = end_date
		self.__option = option

	
	def start_application_by_mode(self):
		if self.__mode == 'minmax':
			minmax = MinMaxTask(self.__currency, self.__currency_expressed_value, self.__start_date, self.__end_date, self.path_to_db)
			minmax.get_minmax_values()
			return str(minmax)
		elif self.__mode == 'list':
			list_task = ListTask(self.__currency,
					self.__currency_expressed_value,
					self.__start_date,
					self.__end_date,
					self.path_to_db,
					limit = self.__option)
			list_task.get_limited()
			return str(list_task)



