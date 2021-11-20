number = int(input('Введите число'))
day = number // 86400
min = number // 60 % 60
sec = number % 86400
hour = sec // 3600 % 3600
sec %= 60

print(('{}дней {} часа {}минута {}секунд'.format(day,hour,min,sec)))