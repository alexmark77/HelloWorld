import pickle
person = {'name':'Alex','phones':[123,345],'age':20}
with open('person_pickle.dat','wb') as f:
    pickle.dump(person,f)
print('End')