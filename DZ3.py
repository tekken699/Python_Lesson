from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number, repeat=False):
    """
    Функция которая формирует из списков случайные шутки!

    :param number = Параметр указывающий на количество шуток
    :param repeat = Параметр указывающий на то уникальные шутки нужны,либо нет
    """

    noun, adver, adjec = nouns.copy(), adverbs.copy(), adjectives.copy()
    new_jokes = []
    min_jokes = min(noun, adver, adjec)

    while number and len(min_jokes):
        num = randrange(len(min_jokes))
        if repeat:
            new_jokes.append(f'{noun.pop(num)} {adver.pop(num)} {adjec.pop(num)}')
        else:
            new_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)} ')
        number -= 1
    return new_jokes


print(get_jokes(2, True))












# def get_jokes(repeat=False):
#     jokes_one = []
#     jokes_two = []
#     for i in sume:
#         jokes_one.append(choice(i))
#         jokes_two.append(choice(q))
#             if repeat:
#
#             else:
#                 jokes_two.append(choice(i))
#
#     print(jokes_one,jokes_two)
# get_jokes()



# def get_jokes(repeat=False):
#     new_jokes = [f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"']
#     sume = [f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"']
#     for i in sume:
#         if repeat:
#             new_jokes = [f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"']
#             sume = [f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"']
#             print(new_jokes,sume)
#         else:
#             new_jokes = [f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"']
#             sume = [f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"']
#             print(new_jokes,sume)
# get_jokes(2)