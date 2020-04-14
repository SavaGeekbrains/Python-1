vyruchka = int(input('Введите сумму  выручку фирмы : '))
izderchki = int(input('Введите сумму  издержек фирмы  : '))
doxod = (vyruchka - izderchki)
if doxod > 0:
    print('Прибыль фирмы больше издержек ')
    print('Рентабельность  равна : ' + str(doxod/vyruchka))
    sotrudniky = int(input('Введите число сотрудников : '))
    print ('Доход фирмы в расчете на одного сотрудника составляет :' + str(doxod/sotrudniky))

if doxod < 0:
    print('Фирма работает в убыток')
if doxod ==0:
    print('Фирма работает в 0')