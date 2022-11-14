import os
import N10_add_remove_folders as arf
from N10_select_element import select_element as se
from N10_print_dir import f_listdir as pd

list = [1, 2, 3, 4]
#list = []
element = se(list)
print(element)

dir = os.getcwd()
pd(dir)
for i in range(1, 10):
    arf.create_dir(dir, 'Dir', i)
pd(dir)
for i in range(1,10):
    arf.delete_dir(dir, 'Dir', i)
pd(dir)