person = {'name':'Alex','phones':[123,345]}
with open('person.dat', 'wb') as f:
    name = person['name']
    f.write(f'{name}\n'.encode('utf-8'))
    phones = person['phones']
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))
print('end')