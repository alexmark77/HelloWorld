number = int(input('Введите число '))
result = None
try:
    result = 100 / number
except ZeroDivisionError as e:
#    result = None
    print('Деление на 0', e)
except Exception:
    print('Неизвестная ошибка')
else:
    print('Ошибок нет', result)
finally:
    print('Конец')
#print(result or 'Деление на 0')

raise Exception ('Создали исключение')