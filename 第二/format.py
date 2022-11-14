
fruits = ["яблоко", "банан", "киви", "арбуз", "персики"]

length = 0
# for fruit in fruits:
#     if len(fruit) > length:
#         length = len(fruit)

length = len(max(fruits, key=len))
# max() - возвращает максимальное значение, для строк выбирает по коду ASCII
# max('aa', 'z')  ->  'z'
# print(length)

i = 1
for fruit in fruits:
    string = f'{i} {fruit.capitalize().rjust(length)}'
    print(string)
    i += 1

print(list(enumerate(fruits, start=1)))
print(list(range(1,6)))

my_list_1 = [2, 5, 8, 2, 12, 12, 4]

for i in range(len(my_list_1)):
    my_list_1[i] = my_list_1[i] / 4 if not(my_list_1[i] % 2) else my_list_1[i] * 2
print(my_list_1)

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
res = [i * 2 if i % 2 else i / 4 for i in my_list_1]

print(my_list_1)
print(res)
