import pickle
with open('person_pickle.dat','rb') as f:
    person = pickle.load(f)
print(person)