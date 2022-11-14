import os

def create_dir(dir, name_f, i):
#    new_f = dir + '/{}_{}'.format(name_f, i)
    new_f = os.path.join(dir, '{}_{}'.format(name_f, i))
    os.mkdir(new_f)

def delete_dir(dir, name_f, i):
    new_f = os.path.join(dir, '{}_{}'.format(name_f, i))
    os.rmdir(new_f)