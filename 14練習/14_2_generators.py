# Выбрать только положительные числа
numbers = [1, 2, 3, 4, 5, -1, -2, -3, -4]

# Класcический способ
res1 = []
for i in numbers:
    if i > 0:
        res1.append(i)
print(res1)

# Через фильтр
res2 = []
res2 = filter(lambda i: i > 0, numbers)
print(list(res2))

# Через генератор
res3 = []
res3 = [num for num in numbers if num > 0]
print(res3)

# Генератор словаря
pairs = [(1, 'a'), (2, 'b'), (3,'c')] # список кортежей
print(type(pairs), pairs)
# Класcический способ
res4 = {}
for i in pairs:
    key = i[0]
    val = i[1]
    res4[key] = val
print(type(res4), res4)

# # Генератор словаря Через генератор
res5 = {}
res5 = {i[0]: i[1] for i in pairs}
print(type(res5), res5)

# Создать список из десяти случайных чисел от 0 до 100
import random
res6 = []
res6 = [random.randint(0,100) for i in range(10)]
print(res6)

# Возвести числа списка в квадрат
res7 = []
res7 = [i**2 for i in res6]
print(res7)

# Выбор имен на букву "А"
names = ['Рус', 'Ант', 'Дми', 'Але', 'Анд', 'Дан']
names_A = [name for name in names if name.startswith('А')]
print(names_A)
names_D = [name for name in names if name[0] == 'Д']
print(names_D)