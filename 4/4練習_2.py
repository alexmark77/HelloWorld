days_dict = {1:'первое',2:'второе',3:'третье',4:'четвертое',5:'пятое',6:'шестое',
        7:'седьмое',8:'восьмое',9:'девятое',10:'десятое',11:'одинадцатое',12:'двенадцатое',
        13:'тринадцатое',14:'четырнадцатое',15:'пятнадцатое',16:'шетьнадцатое',17:'семьнадцатое',
        18:'восемьнадцатое',19:'девятнадцатое',20:'двадцатое',30:'тридцатое'}
days10_dict = {20:'двадцать',30:'тридцать'}
months_dict = {1:'января',2:'февраля',3:'марта',4:'апреля',5:'мая',6:'июня',
        7:'июля',8:'августа',9:'сентября',10:'октября',11:'ноября',12:'декабря'}

data = input('Введите дату в формате DD.MM.EEEE ')
data_list = data.split('.')
day = int(data_list[0])
month = int(data_list[1])
print(data_list[2])

print(day, month)

day01 = day % 10
day10 = day - day01
print('day01=',day01, ' day10=',day10)
if day <= 20 or day01 == 0:
    day_print = days_dict.get(day)
else:
    day_print = days10_dict.get(day10) + ' ' + days_dict.get(day01)
resault = f'{day_print} {months_dict.get(month)} {data_list[2]} года'
#print(day_print, months_dict.get(month), data_list[2], 'года')
print(resault)