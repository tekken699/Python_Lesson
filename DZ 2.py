class DivisionEX(ZeroDivisionError):
    def __init__(self, text):
        self.text = text

def incorrect(a, b):
    if b == 0:
        raise DivisionEX('Деление на ноль')
    return a / b

try:
    print(incorrect(1,0))
except DivisionEX:
    print('Деление на ноль')