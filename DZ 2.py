tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', ]

num = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None)for i in range(len(tutors)))


print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(type(num))
print(list(num))




#print(num)
# for key, numm in zip(tutors, klasses):
#
#
#     num[key] = numm
#
# #print(num)
#

