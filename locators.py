from selenium.webdriver.common.by import By

class CurrencyDataLocators(): # уточнить вынести ли в отдельный ф
	NAME = (By.CSS_SELECTOR,'.symbol .name')
	PRICE = (By.CSS_SELECTOR,'.last-block .last')


class FrameSwitchingLocators():
	pass