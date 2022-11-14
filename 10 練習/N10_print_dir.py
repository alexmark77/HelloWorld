from os import listdir

def f_listdir(dir):
    print(dir, ': ')
    print(listdir(dir))
    # for i in os.listdir(dir):
    #     print(i)