class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['()' * rows for i in range(self.nums // rows)]) + '\n' + '()' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Sum if Cell is :')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Substraction of cell is :')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Ячеек во второй меньше чем в первой'

    def __mul__(self, other):
        print('Multiply of cell is:')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Truediv of cell is: ')
        return Cell(self.nums // other.nums)

cell_1 = Cell(55)
cell_2 = Cell(23)

print(cell_2.make_order(45))
print(cell_1 - cell_2)