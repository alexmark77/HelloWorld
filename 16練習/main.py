from core import create_file, create_folder, get_list, delete_file, copy_file, save_info
import sys

#get_list()

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'cr_file':
    pass
elif command == 'cr_fold':
    pass
elif command == 'del_file':
    pass
elif command == 'del_fold':
    pass
elif command == 'copy':
    pass
elif command == 'save':
    pass
else:
    print('Помощь')