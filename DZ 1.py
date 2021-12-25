A = [[2, 4, 2, 4], [2, 5, 5, 6], [3, 6, 1, 1], [5, 7, 8, 6]]
B = [[6, 6, 3, 1], [6, 7, 8, 2], [0, 0, 5, 5], [6, 1, 1, 9]]

class Matrix:
    def __init__(self,list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(lambda r:'  '.join(map(str, r)), self.list)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2:map(lambda x, y: x + y, r_1, r_2), self.list, other.list))

matrix_1 = Matrix(A)
matrix_2 = Matrix(B)

print(matrix_1)
print(matrix_2)

sum_matrix = matrix_1 + matrix_2
print(sum_matrix)