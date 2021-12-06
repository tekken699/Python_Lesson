def gener_num(num):
    for i in range(1, num + 1):
        if i % 2 == 1:
            yield i


step = gener_num(10)

print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))
