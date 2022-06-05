from typing import List
from rates import Rates

class Normalizer():
	def __init__(self,raw_value:List[Rates]) -> None:
		self.__raw_value = raw_value


	def normalize(self)->List[Rates]:
		result = []
		for rates in self.__raw_value:
			if rates.currency == 'USD':
				new_val = 1/rates.value
				new_rates = Rates(rates.currency_expressed_value,rates.currency,new_val,rates.date)
				result.append(new_rates)
			elif rates.currency_expressed_value == 'USD':
				result.append(rates)
			else:
				continue

		return result
