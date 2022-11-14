import os

import N10_add_remove_folders as arf

# Создание 9-и папок Dir_1 ... Dir_9

dir = os.getcwd()
f_listdir(dir)
for i in range(1, 10):
    arf.create_dir(dir, 'Dir', i)
f_listdir(dir)

for i in range(1,10):
    arf.delete_dir(dir, 'Dir', i)

f_listdir(dir)