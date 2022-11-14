# import modA
# from mods.modB import string, function
# import mods.modC
#
# print(modA.string)
# modA.function()
#
# print(string)
# function()

# from Hospital.hos import get_main
# from Hospital.pacients.index import  get_index
# get_main()
# get_index()

# import os
# print(os.name)
# print(os.getcwd())
# new_path = os.path.join(os.getcwd(),'new_f')
# os.mkdir(new_path)

# import sys
# print(sys.executable)
# print(sys.platform)
# sys.exit()
# print('Этот код не выполняется')

# import sys
# print(sys.path)
# print(type(sys.path))
#
# for p in sys.path:
#     print(p)
#
# sys.path.append('Z:')
# import module
# for p in sys.path:
#     print(p)

#例えば

import sys, os
name_sys = sys.platform
dir = os.getcwd()
for i in range(1,6):
    new_folder = os.path.join(dir,'{}_{}'.format(name_sys,i))
    os.mkdir(new_folder)