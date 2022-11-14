# 1
equation = 'y = -12x + 11'
x = 2.5

def messeg_error():
    print('Неверный вид выражения "y = ax + b"')
try:
    _, _, ax, _, b = equation.split()
except:
    messeg_error
else:
    print(ax, b)
    if ax[-1] != 'x':
        messeg_error
    else:
        a = float(ax[:-1])
        b = float(b)
        print(a * x + b)

# 2
def data_out(day, month, years):
    days_dict = {1:'первое',2:'второе',3:'третье',4:'четвертое',5:'пятое',6:'шестое',
            7:'седьмое',8:'восьмое',9:'девятое',10:'десятое',11:'одинадцатое',12:'двенадцатое',
            13:'тринадцатое',14:'четырнадцатое',15:'пятнадцатое',16:'шетьнадцатое',17:'семьнадцатое',
            18:'восемьнадцатое',19:'девятнадцатое',20:'двадцатое',30:'тридцатое'}
    days10_dict = {20:'двадцать',30:'тридцать'}
    months_dict = {1:'января',2:'февраля',3:'марта',4:'апреля',5:'мая',6:'июня',
            7:'июля',8:'августа',9:'сентября',10:'октября',11:'ноября',12:'декабря'}
    day01 = day % 10
    day10 = day - day01
    # print('day01=',day01, ' day10=',day10)
    if day <= 20 or day01 == 0:
        day_print = days_dict.get(day)
    else:
        day_print = days10_dict.get(day10) + ' ' + days_dict.get(day01)
    resault = f'{day_print} {months_dict.get(month)} {years} года'
    #print(day_print, months_dict.get(month), data_list[2], 'года')
    print(resault)



while True:
    ddmmyyyy = input('Введите дату в формате DD.MM.YYYY ')
    d, m, y = ddmmyyyy.split('.')
    d = int(d)
    m = int(m)
    y = int(y)
    # print(d, m, y)
    if y < 0 or y > 9999:
        print('Год должен быть от 0000 до 9999')
        continue
    if m < 1 or m > 12:
        print('Месяц д.б. от 01 до 12')
        continue
    m30 = [4, 6, 9, 11]
    m28 = 2
    if d < 1 or d > 31:
        print('Число д.б. от 01 до 31')
        continue
    elif d > 28 and m == m28:
        print('В февлале д.б. 28 дней')
        continue
    elif d > 30 and m in m30:
        print('В указанном вами месяце только 30 дней')
        continue
    else:
        break
data_out(d, m, y)
# print(f'Ваша дата: {d}.{m}.{y}')
