from rates import Rates

class CrossRates():
	def __init__(self,rates1: Rates, rates2: Rates) -> None:
		self.__rates1 = rates1 #rename
		self.__rates2 = rates2 #rename


	def get_rates1_by_rates2(self)->Rates: #rename
		return Rates(self.__rates1.currency,
						self.__rates2.currency,
						self.__rates1.value / self.__rates2.value,
						self.__rates1.date)