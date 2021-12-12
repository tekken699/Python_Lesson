import requests

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
res = response.text.split("Valute")


def currency_rates():
    valute = input("Ввидите название валюты")
    for i in res:
        if valute.upper() in i:
            print(valute.upper(), i.replace("/", "").split("<Value>")[-2])
        elif valute.lower() in i:
            print(valute.upper(), i.replace("/", "").split("<Value>")[-2])


currency_rates()






# response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
# valute = input('Введите валюту')
# res = response.text.split("Valute")
#
#
# def currency_rates():
#     for i in res:
#         if valute.upper() in i:
#             print(valute.upper(), i.replace("/", "").replace(">", "").replace("<", "").split("Value")[-2])
#         elif valute.lower() in i:
#             print(valute.upper(), i.replace("/", "").replace(">", "").replace("<", "").split("Value")[-2])
#
# currency_rates()