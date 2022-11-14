with open('person.dat','r',encoding='utf-8') as f:
    result = f.readlines()
person = {}
person['name'] = result[0].replace('\n','')

phones = []
for phone in result[1:]:
    phones.append(f'{phone}'.replace('\n',''))
person['phones'] = phones

print(person)