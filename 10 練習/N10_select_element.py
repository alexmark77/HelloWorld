from random import choice

def select_element(list):
# #    if len(list) == 0:
#     if list == []:
#         return (None)
#     else:
#         a = choice(list)
#         return (a)

    if list:
        el = choice(list)
        return el


# Проверка модуля
if __name__ == '__main__':
    list = [1, 2, 3, 4]
    # list = []
    element = select_element(list)
    print(element)