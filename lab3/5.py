a = []

for i in range(8):
    num = None

    while num is None:
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("Ошибка! Введите целое число")

    a.append(num)

for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2

print("Преобразованный массив:", a)