# *Задание в группах:** Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 
# - *под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель*
# *Фамилия_1*
# *Имя_1*
# *Телефон_1*
# *Описание_1*
# *Фамилия_2*
# *Имя_2*
# *Телефон_2*
# *Описание_2*
# *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***
# *Фамилия_1,Имя_1,Телефон_1,Описание_1*
# *Фамилия_2,Имя_2,Телефон_2,Описание_2*
# *и т.д.*
# ❗ Можно явно указать на использование CSV
# *Если группа сильная, можно предложить внедрить JSON, XML*

import controller as c

print(
'1. Запуск калькулятора комплексных чисел\n' +
'2. Запуск калькулятора рациональных чисел\n' + 
'3. Просмотр логов\n' +
'4. Выход\n')
c.getResult()