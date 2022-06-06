# AlphaInsurance_test_case

В файле parser.py запускается парсинг страницы https://ru.investing.com/charts/forex-charts; с последующей выгрузкой в rates_db.db. Для экономии места в БД, принято решение о использовании универсальной валюты - USD.

Из файла main.py запускается консольное приложение. 
Примеры запуска:
python.exe .\main.py list USD RUB 2022-06-05 2022-06-06 --limit=4  
Count = 2
1. 60.95
2. 60.95

python.exe .\main.py minmax USD RUB 2022-06-05 2022-06-06
MIN = 60.95
MAX = 60.95

