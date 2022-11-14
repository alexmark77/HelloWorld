#Открытие или создание-открытие файла
f = open('first.txt', 'w')

# Открытие только существующего файла, иначе ошибка
#f = open('second.txt', 'r')

# Запись текста в файл
f.write('Hello\n')
f.write('World\n')

# Запись списка в файл \n в конце стороки обязателен
list=['Good moning\n', 'Alex\n']
f.writelines(list)