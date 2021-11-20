a = 'Процент'
b = 'Процентов'
c = 'Процента'
contin = int(input('Нажмите Ентер!'))
numbers = {11,12,13,14}
for i in range(0,100):
    i +=1
    if i in numbers:
        print(i,b)
    elif i % 10 ==1:
        print(i,a)
    elif i % 10 ==0:
        print(i,b)
    elif i % 10 >1 and i % 10 <5:
        print(i,c)
    else:
        print(i,b)


# num = int(input('Введите цифру!'))
# numbers = {11,12,13,14}
# if num in numbers:
#     print(num, 'Процентов')
# elif num % 10 == 1:
#     print(num, 'Процент')
# elif num % 10 ==0:
#     print(num, 'Процентов')
# elif num % 10 >1 and num % 10 <5:
#     print(num, 'Процента')
# else:
#     print(num, 'Процентов')
