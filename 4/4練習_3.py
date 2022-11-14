my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = []
print(my_list_1)
for i in my_list_1:
    if my_list_1.count(i) == 1:
        my_list_2.append(i)
print(my_list_2)

my_list_1 = [3, 5, 5, 5, 5, 4,  2, 2, 5, 12, 8, 2, 12, 13]
my_list_2 = []
print(my_list_1)
for i in my_list_1:
    print('for ',i)
    if not(my_list_1.count(i) == 1):
        while i in my_list_1:
            print('while',i)
            my_list_1.remove(i)
print(my_list_1)
