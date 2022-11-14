#import reduce
# def input_data(name, age, city):
#     name = input('Введите Ваше имя: ')
#     age = input('Введите ваш возраст: ')
#     city = input('Введите город проживания: ')
#     return(f'{name}, {age} год(а), проживает в городе {city}')
#
# print(input_data('Вася', 22, 'Москва'))

# def max_number(a, b, c):
#     result = max([a, b, c])
#     numbers = [a, b, c]
#     #numbers.append(a)
#     #numbers.append(b)
#     #numbers.append(c)
#     # print(max(numbers))
#     print(reduce(max, numbers))
#
# max_number(1, 5, 3)

name = 'A' #input('Введите имя героя ')
hero = {
    'name':name,
    'health':100,
    'damage':50,
    'armor':1.2
}
name = 'B' #input('Введите имя врага ')
enemy = {
    'name':name,
    'health':100,
    'damage':50
}
print(enemy)
enemy['armor'] = 1.6
print(enemy)

def get_damage(damage,armor):
    return damage / armor

def attack (unit, target):
#    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= unit['damage'] / target['armor'] #damage
    return

attack (hero, enemy)
print(enemy)
attack (enemy, hero)
print(hero)
