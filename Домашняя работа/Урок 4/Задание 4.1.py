from sys import argv

name,time, salary, bonus = argv
try:
    time = int(time)#40
    salary = int(salary)#1000
    bonus = int(bonus)#500
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
     print('Не число')