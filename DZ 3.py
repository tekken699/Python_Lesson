import requests

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
res = response.text.split("Valute")
date = 'Date'


def currency_rates():
    valute = input("Введите название валюты!")
    for i in res:
        if valute.upper() in i:
            print(valute.upper(), i.replace("/", "").split("<Value>")[-2])
        elif valute.lower() in i:
            print(valute.upper(), i.replace("/", "").split("<Value>")[-2])
        if date in i:
            print(i.split(" ")[-4], end=" ")


currency_rates()