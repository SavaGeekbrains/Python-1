a = float(input("Результат первого дня : "))
b = float(input("Цель которую хотите достичь :"))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)
