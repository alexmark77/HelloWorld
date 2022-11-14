
list_test = [('New',1500,'Ame'),
             ('Mos',1000,'Rus'),
             ('Toc',500,'Jap')
             ]

print(list_test)
print(sorted(list_test))

def found_key(x):
    print(x[1])
    return x[1]
print(sorted(list_test,key=found_key))

print(sorted(list_test,key=lambda x: x[0]))

