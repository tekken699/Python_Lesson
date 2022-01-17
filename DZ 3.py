b = []

class TyEx(TypeError):
    pass

while True: 
    a = input('Введите число')
    try:
        if a.isdigit():
            b.append(a)
        elif a == 'Stop':
            break
        else:
            raise TyEx()
    except TyEx as err:
        print('Введено не число')
print(b)