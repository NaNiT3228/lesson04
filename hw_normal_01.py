# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

name_pattern = '[A-ZА-Я][a-zа-я]+'
surname_patten = '[A-ZА-Я][a-zа-я]+'
email_pattern = '[a-zA-z0-9_]+@[a-z0-9]+\.(ru|org|com)'

surname = input('Введите фамилию: ')
name = input('Введите имя: ')
email = input('Введите email: ')

surname_res = re.match(surname_patten, surname)
name_res = re.match(name_pattern, name)
email_res = re.match(email_pattern, email)

if surname_res:
    if name_res:
        if email_res:
            print('Данные верны')
        else:
            print('Некорректный email')
    else:
        print('Неправильно введено имя')
else:
    print('Неправильно введена фамилия')
