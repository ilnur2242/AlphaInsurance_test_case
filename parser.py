from tasks.investing_task import InvestingComWriter
from database import DataBaseConnector
from selenium import webdriver
import sqlite3
from sqlite3 import Error

PATH_TO_DATABASE = 'C:\\Users\\valiu\\AlphaInsurance_test_case\\rates_db.db'
BROWSER = webdriver.Chrome()

def main():
	investingComWriter = InvestingComWriter(PATH_TO_DATABASE,BROWSER)
	investingComWriter.write_investing_com()

main()

