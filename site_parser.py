import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import CurrencyDataLocators
from selenium.common.exceptions import NoSuchElementException
import time
from rates import Rates
from datetime import date
from typing import List


TIME_TO_SLEEP = 6


class InvestingComParser(): # rename inv com parser

	def __init__(self, browser,timeout=10) -> None:
		self.__url = 'https://ru.investing.com/charts/forex-charts'
		self.__browser = browser # Вытащить вебраузер в парамертры, чтоб юзер мог сам быбрать браузер; dependens injection
		# можно ли перезаписать свойстро; public, private
		self.__browser.get(self.__url)
		self.__browser.implicitly_wait(timeout)


	def __switch_frames(self): # 
		iframe = self.__browser.find_element(By.CSS_SELECTOR, 'iframe[seamless]')
		self.__browser.switch_to.frame(iframe)
		time.sleep(TIME_TO_SLEEP)
		iframe = self.__browser.find_element(By.CSS_SELECTOR, 'iframe[seamless]')
		self.__browser.switch_to.frame(iframe)
		time.sleep(TIME_TO_SLEEP)
		iframe = self.__browser.find_element(By.CSS_SELECTOR, 'iframe[id][name]')
		self.__browser.switch_to.frame(iframe)
		time.sleep(TIME_TO_SLEEP)


	def __createRates(self,currency_ratio:str, price:float):
		name = currency_ratio.split('/')
		currency, currency_expressed_value = ('','')
		if len(name) > 1:
			currency, currency_expressed_value = name
		else:
			return ''
		today = date.today()
		rates = Rates(currency, currency_expressed_value,price,today)
		return rates


	def get_rates(self):
		 # rename it
		self.__switch_frames()
		name_selectors =  self.__browser.find_elements(*CurrencyDataLocators.NAME)
		price_selectors = self.__browser.find_elements(*CurrencyDataLocators.PRICE)
		
		result: List[Rates] = []
		for name_selector,price_selector in zip(name_selectors,price_selectors):
			currency_ratio = name_selector.text
			price = float(price_selector.text)
			rates = self.__createRates(currency_ratio,price)
			if rates != '':
				result.append(rates)
			

		return result

	def __str__(self):
		return 'InvestingComParser'

	def __del__(self):
		self.__browser.close()

""" def is_element_present(browser:webdriver, how, what):
	try:
		browser.find_element(how, what)
	except NoSuchElementException:
		return False
	return True


url = 'https://ru.investing.com/charts/forex-charts'
try:
	browser = webdriver.Chrome()
	browser.get(url)
	browser.implicitly_wait(30)

	data = []
	
	iframe = browser.find_element(By.CSS_SELECTOR,'iframe[seamless]')
	browser.switch_to.frame(iframe)
	time.sleep(3)
	iframe = browser.find_element(By.CSS_SELECTOR,'iframe[seamless]')
	browser.switch_to.frame(iframe)
	time.sleep(3)
	iframe = browser.find_element(By.CSS_SELECTOR,'iframe[id][name]')
	browser.switch_to.frame(iframe)
	time.sleep(6)
	name_selectors =  browser.find_elements(*CurrencyDataLocators.NAME)
	price_selectors = browser.find_elements(*CurrencyDataLocators.PRICE)
	for name_selector,price_selector in zip(name_selectors,price_selectors):
		print(name_selector.text,price_selector.text)
	print('start sleep')
	

except NoSuchElementException as e:
	print(e)	
		

finally:
	browser.close() """
