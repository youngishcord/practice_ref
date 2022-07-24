import calendar


print('добро пожаловать')

while True:

    year = int(input('пожалуйста введите год: '))
    month = int(input('введите месяц: '))
    if month == 0:
        break
    try:
        print('\n', calendar.month(year, month), end='\n')
    except:
        print('неверный месяц')
        continue
print('всего хорошего')