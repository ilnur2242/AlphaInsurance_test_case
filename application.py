from dataclasses import dataclass
from database import DataBase
from site_parser import Parser
from datetime import date

class Application(): # high level
	def __init__(self,path_to_db,url) -> None:
		#self.db = DataBase(path_to_db)
		self.parser = Parser()
		self.parser.open(url)

	
class ParserApplication(Application): # парсить аргументы командной строки
	def set_currency_data(self):
		data_list = self.parser.get_currency_data()
		today = date.today().strftime('%Y-%m-%d')
		for elem in data_list:
			name = elem['name'].split('/')
			if len(name) > 1:
				currency, currency_expressed_value = name
			else:
				currency, currency_expressed_value = (name[0], 'None')
			price = elem['price']
			print(currency, currency_expressed_value,today,price)




