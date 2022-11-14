# Открытие файла для чтения

f = open('first.txt', 'r')

# чтение всего файла
#print(f.read())

# чтение по строчно
# for line in f:
#     print(line.replace('\n', ''))

# Чтение в список
print(f.readlines())

f.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')