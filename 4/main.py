print('Медицинская анкета')

name = input('お名前は？')
age = int(input('貴方の年齢は？'))
weight = int(input('貴方の体重は？'))

if age <= 30 and (weight >= 50 and weight <= 120):
    print (name,'возраст',age,'вес',weight,'- хорошее состояние')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, 'возраст', age, 'вес', weight, '- следует заняться собой')
elif age > 30 and (weight < 50 or weight > 120):
    print(name, 'возраст', age, 'вес', weight, '- следует обратится к врачу!')
else:
    print('貴方は誰ですか？')
num=0


