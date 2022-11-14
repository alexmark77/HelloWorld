# Открываем файл для работы с байтами

with open('bytes.txt', 'wb') as f:
    f.write(b'Hello World')

with open('bytes.txt', 'rb') as f:
    print(f.read())
    pass
with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

with open('bytes.txt', 'wb') as f:
    # str_b = 'Привет 世界'   # ОШИБКА
    str_b = 'Привет 世界'.encode('utf-8')
    f.write(str_b)
    # str = 'Привет 世界'
    # f.write(str.encode('utf-8'))
with open('bytes.txt', 'rb') as f:
    str_b = f.read()
    print(type(str_b), str_b)
    str = str_b.decode('utf-8')
    print(str)
with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open('bytes.txt', 'w', encoding='utf-8') as f:
    str = 'Привет 世界'
    f.write(str)
with open('bytes.txt', 'r') as f:
    str = f.read()
    # print(str.decode('utf-8')) # ОШИБКА
    print(str) # Непонятные символы РџСЂРёРІРµС‚ дё–з•Њ
    str_b = str.encode('utf-8')
    print(type(str_b), str_b)

with open('bytes.txt', 'r', encoding='utf-8') as f:
    str = f.read()
    print(type(str), str)