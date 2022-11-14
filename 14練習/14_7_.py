# фркуты
a = ['яблоки', 'апельсины', 'мандарины', 'гранаты', 'бананы']
b = ['манго', 'апельсины', 'киви', 'груши', 'бананы']
res = []
res = [i for i in b if i in a] #
print(res)

# Числа
import random
a = [random.randint(-100,100) for i in range(20)]
a_3 = [i for i in a if i % 3 == 0]
a_p = [i for i in a if i > 0]
a_4 = [i for i in a if i % 4 != 0]
a_4_2 = [i for i in a if i > 0 and i % 3 == 0 and i % 4 != 0]
print(a, '\n', a_3, '\n', a_p, '\n', a_4, '\n', a_4_2)

import math
def sqrt_list(input_list):
    res = [(math.sqrt(i) if i > 0 else i) for i in input_list]
    return res

b = sqrt_list(a)
print(b)

def sqrt_number(imput_number):
    if imput_number == 13:
        raise ValueError('Тринадцать')
    else:
        return (imput_number ** 2)

number = int(input('Введите число от 0 до 100 '))

try:
    print(sqrt_number(number))
except ValueError:
    print('А-а-а!!! Тринадцать')

