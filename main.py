from application import CosoleApplication
import click
from selenium import webdriver
from datetime import date

PATH_TO_DATABASE = 'C:\\Users\\valiu\\AlphaInsurance_test_case\\rates_db.db'

@click.command()
@click.argument('mode',type=click.Choice(['minmax','list']))
@click.argument('currency')
@click.argument('currency_expressed_value',default='USD')
@click.argument('start_date')
@click.argument('end_date')
@click.option('--limit', default=1)
def main(mode,currency,currency_expressed_value,start_date,end_date,limit):
	start_date = date(*[int(elem) for elem in start_date.split('-')])
	end_date = date(*[int(elem) for elem in end_date.split('-')])

	result = CosoleApplication(PATH_TO_DATABASE,
						mode,
						currency,
						start_date,
						end_date,
						int(limit),
						currency_expressed_value=currency_expressed_value
						).start_application_by_mode()
	print(result)
	#print(mode,currency,currency_expressed_value,start_date,end_date,limit)
	

if __name__ == '__main__':
	main()
