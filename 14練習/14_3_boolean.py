str = 'Alex'
if str:
    print('Строка не пустая', len(str))
else:
    print('Строка пустая', len(str))

import math

# оператор AND
if 1 > 2 and math.sqrt(-1):
    pass
else:
    print('Ошибки нет, т.к. первое условие False, а дальше Python не проверяет')
# if math.sqrt(-1) and 1 > 2:
#     pass
# else:
#     print('Ошибка есть, т.к. первое условие False извлечение кв. корня из минус 1')
print([1] and [] and '' and 1.1)        # Возвращает [] - первый False
print([1] and [2] and 'a' and 1.1)      # Возвращает 1.1 - последний True

# оператор OR
if 1 < 2 or math.sqrt(-1):
    print('Ошибки нет, т.к. первое условие True, а дальше Python не проверяет')
print([1] or [] or '' or 1.1)        # Возвращает [1] - первый True
print([] or [] or '' or 1.1)      # Возвращает 1.1 - первый True
print([] or [] or '' or {})      # Возвращает 1.1 - последний False
