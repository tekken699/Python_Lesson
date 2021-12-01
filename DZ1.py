# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# , как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate(num):

    number = {
        'one':'один',
        'two': 'два',
        'tree': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eith': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    return number.get(num)


while True:
    enter = input('Введите число')
    print(num_translate(enter))
    if enter == 'ext':
        break
