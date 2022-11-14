import os
print(os.getcwd())
# os.mkdir('test_f')
print(os.getcwd())
os.chdir('test_f')
print(os.getcwd())

folder, file = os.path.split(os.getcwd())
print(type(folder), folder)
os.chdir(folder)
print(os.getcwd())
