import pickle, json
my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['ASS Последний месяц осени', 'Шапито'],
    'Albums': [ {'name': 'Делать панк-рок','year': 2016},
                {'name': 'Шапито','year': 2014}]
}

mfg_pickle = pickle.dumps(my_favourite_group)
print(1, type(mfg_pickle), mfg_pickle)
mfg_str = json.dumps(my_favourite_group)
print(3, type(mfg_str), mfg_str)

with open('mfg_pickle.dat','wb') as f:
    f.write(mfg_pickle)
#    pickle.dump(my_favourite_group, f)
with open('mfg.json', 'w', encoding='utf-8') as f:
    f.write(mfg_str)
#    json.dump(my_favourite_group, f)


