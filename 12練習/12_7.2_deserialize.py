import pickle, json

with open('mfg_pickle.dat','rb') as f:
    mfg_pickle2 = pickle.load(f)
print(2, type(mfg_pickle2), mfg_pickle2)

with open('mfg.json', 'r', encoding='utf-8') as f:
    mfg_str2 = json.load(f)
print(4, type(mfg_str2), mfg_str2)
