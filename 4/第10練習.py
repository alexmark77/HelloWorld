# 1. Длинна окружности радиусом r
import math
r = 5 #int(input('Введите радиус окружности '))
print('Диаметр = ', r*2)
print('Длинна окружности = ', 2 * math.pi * r )
print('Площать окружности = ', math.pi * math.pow(r,2))
x1 = 100
y1 = 200
x2 = 150
y2 = 250
print(math.sqrt((x1-x2)**2 + (y1-y2)**2))
print(math.factorial(9))

from random import randint, choice, sample, shuffle
print(randint(5,10))
mounth = ['января','февраля','марта','апреля','мая','июня',
        'июля','августа','сентября','октября','ноября','декабря']
print(choice(mounth))
print(sample(mounth,3))
print(mounth)
shuffle(mounth)
print(mounth)