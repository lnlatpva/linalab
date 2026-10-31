a = list(map(int, input('Введите числа:').split()))
for i in range(len(a)):
    for k in range(i + 1, len(a)):
        if a[i] == a[k]:
            print('Эллемент:', a[i], 'Индексы', i, k) # Вариант 13.1
for i in range(len(a)):
    if a[i] < 15:
        a[i] = a[i] * 2
print('Преобразованный массив', a)