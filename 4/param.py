import os, sys
# for arg in sys.argv:
#     print(arg)
#     print(type(arg))

def f_ping():
    print('pong')

def f_hello(name):
    print('Привет {}'.format(name))

def f_listdir():
    dir = os.getcwd()
#    dir = 'Z:'
    print(dir)
    for i in os.listdir(dir):
        print(i)

if sys.argv[1] == 'ping':
    f_ping()
elif sys.argv[1] == 'name':
    f_hello(sys.argv[2])
elif sys.argv[1] == 'list':
    f_listdir()
