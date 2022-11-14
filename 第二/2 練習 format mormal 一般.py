list_a = [2, -5, 8, 9, -25, 25, 4]
list_b = []
list_c = []
import math

# print(float.is_integer(15.1)) # False
# x = 10.1
# print(x == int(x)) # False
# x = 10
# print(x == int(x)) # True


# math.sqrt(x) == x ** 0.5
# float.is_integer(x)  если x - float, то возвращает True
for i in list_a:
    if i > 0 and float.is_integer(math.sqrt(i)):
        list_b.append(int(math.sqrt(i)))
print(list_b)

# list_c = [int(math.sqrt(i)) if i > 0 and float.is_integer(math.sqrt(i)) else XXXXXXX for i in list_a]
print(list_c)

# print(float.is_integer(float(15)))

# 4
list_a = [1, 2, 3, 4, 4, 5, 5, 4, 6, 6, 7, 8, 9]
list_b = []

for i in list_a:
    if list_a.count(i) == 1:
        list_b.append(i)
print(list_b)