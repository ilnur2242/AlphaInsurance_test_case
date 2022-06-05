

from datetime import date
from datetime import date

class Rates():
	def __init__(self,cur: str, currency_expressed_value: str, val: float, date: date) -> None:
		self.__currency = cur
		self.__currency_expressed_value = currency_expressed_value
		self.__value = val
		self.__date = date

	@property
	def currency(self):
		return self.__currency

	
	@property
	def currency_expressed_value(self):
		return self.__currency_expressed_value

	
	@property
	def value(self):
		return self.__value

	
	@property
	def date(self):
		return self.__date