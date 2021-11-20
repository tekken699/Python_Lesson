def sum_digits(value):
    result = 0

    while value != 0:
        result += value % 10
        value //= 10

    return result


arr = [i**3 for i in range(1, 1001, 2)]


result1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, arr))
result2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr))

print(result1)
print(result2)