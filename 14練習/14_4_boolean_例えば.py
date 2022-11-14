import math
numbers = [4, 3, 2, 1, -4 , -3, 8, 9]

# Получить список из чисел квабрат корня которых меньше 2-х
# Классический
res = []
for i in numbers:
    if i > 0:
        if math.sqrt(i) < 2:
            res.append(i)
print(res)
# Свойство Python
res = []
for i in numbers:
    if i > 0 and math.sqrt(i) < 2:
        res.append(i)
print(res)
# Через генератор
res = []
res = [i for i in numbers if i > 0 and math.sqrt(i) < 2]
print(res)

# Добавить в список элемент
# Классический
def add_to_list(imput_list=None): # Если не передавать папаметр, то присвоить значение None
    if imput_list is None:
        imput_list = []
    imput_list.append(2)
    return (imput_list)

print(add_to_list([1,3]))
print(add_to_list())

# Способ с OR
def add_to_list1(imput_list=None): # Если не передавать папаметр, то присвоить значение None
    imput_list = imput_list or []
    imput_list.append(2)
    return (imput_list)

print(add_to_list1([1,3]))
print(add_to_list1())

res = [i ]