is_name = False #True
print('Alex' if is_name else 'Empty')

is_one = False
print(1 if is_one else 2)

is_russian = True
print('Привет' if is_russian else 'Hello')

word = 'KkmxiwejJlkasKKJJHJ'
result = []
for i in range(len(word)):
    # if i % 2 != 0:
    #     letter = word[i].lower()
    # else:
    #     letter = word[i].upper()
    letter = word[i]
    letter = letter.lower() if i % 2 == 0 \
        else letter.upper()
    result.append(letter)
result = ''.join(result)
print(type(result), result)

password = input('Введите пароль: ')
print('Вход' if password == 'asd' else 'Вход запрещен')