import json
person = [
    {'name':'Alex','phones':[123,345],'age':20},
    {'name':'Max','phones':[789,890],'age':22},
    {'name':'Kate','age':19},
]
print(type(person), person)

person_json = json.dumps(person)

with open('person_json.dat', 'w') as f:
    json.dump(person, f)
print(type(person_json), person_json)

with open('person_json.dat', 'r') as f:
    person = json.load(f)
print(type(person), person)