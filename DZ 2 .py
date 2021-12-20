class Road:
    def __init__(self):
        self._length = int(input('Введите длину'))
        self._width = int(input('Введите ширину'))

    def formula(self):
        calculations = self._length * self._width * 25 * 5 // 100
        print(f'{calculations}т Массы асфальта потребуется для покрытия всей дороги')

w = Road()
w.formula() 