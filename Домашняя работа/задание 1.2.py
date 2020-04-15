time = int(input("Введите время в секундах : "))


chas = time // 3600
min = (time // 60) % 60
sec = time % 60

print(f'{chas:02}:{min:02}:{sec:02}')




