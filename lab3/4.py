n = 0

while n <= 0:
    try:
        n = int(input("Количество элементов: "))
        if n <= 0:
            print("Введите положительное число")
    except ValueError:
        print("Введите целое число")
        n = 0

a = []

for i in range(n):
    num = None

    while num is None:
        try:
            num = int(input("Введите элемент: "))
        except ValueError:
            print("Введите целое число")

    a.append(num)

found = False

for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            print("Одинаковые элементы:", a[i])
            print("Индексы:", i, "и", j)
            found = True

if not found:
    print("Одинаковых элементов нет")