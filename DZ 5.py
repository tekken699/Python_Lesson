class Stationery:
    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'{self.tittle} пишет')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.tittle} затупился')

class Handle(Stationery):
    def draw(self):
        print(f'{self.tittle} новый')

a = Handle('Маркер')
a.draw()
v = Pen('Карандаш')
v.draw()
