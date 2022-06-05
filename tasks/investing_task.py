from database import DataBaseConnector
from site_parser import InvestingComParser
from writer import Writer
from normalizer import Normalizer


class InvestingComWriter():
	def __init__(self,path_to_db, browser) -> None:
		self.__path_to_db = path_to_db
		self.__browser = browser

	def write_investing_com(self):
		conn = DataBaseConnector(self.__path_to_db).get_connection()
		investingComParser = InvestingComParser(self.__browser, timeout=30)
		normalizer = Normalizer(_result)
		writer = Writer(conn)

		_result = investingComParser.get_rates()
		normalized_result = normalizer.normalize()
		for elem in normalized_result:
			writer.write_new_row(elem)



