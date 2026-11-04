f1 = True
while f1:
    try:
        mat_choice_str = input("Выберите материал (1 — сталь, 2 — алюминий, 3 — медь): ")
        mat_choice = int(mat_choice_str)

        if mat_choice not in (1, 2, 3):
            raise ValueError("Некорректный выбор материала.")

        f1 = False

    except ValueError:
        print("Ошибка ввода: выберите 1, 2 или 3 и попробуйте снова.")

match mat_choice:
    case 1:
        material, alpha = "сталь", 1.2e-5
    case 2:
        material, alpha = "алюминий", 2.3e-5
    case 3:
        material, alpha = "медь", 1.7e-5

f2 = True
while f2:
    try:
        L0 = float(input("Введите начальную длину (1-10000 мм): "))

        if 1 <= L0 <= 10000:
            f2 = False
        else:
            print("Ошибка: длина должна быть от 1 до 10000 мм")
    except ValueError:
        print("Ошибка: введите число")


f3 = True
while f3:
    try:
        t1 = float(input("Введите начальную температуру (-60...200 °C): "))

        if -60 <= t1 <= 200:
            f3 = False
        else:
            print("Ошибка: температура должна быть от -60 до 200 °C")
    except ValueError:
        print("Ошибка: введите число")

f4 = True
while f4:
    try:
        t2 = float(input("Введите конечную температуру (-60...800 °C): "))

        if -60 <= t2 <= 800:
            if t2 > t1:
                f4 = False
            else:
                print("Ошибка: t2 должна быть больше t1")
        else:
            print("Ошибка: температура должна быть от -60 до 800 °C")
    except ValueError:
        print("Ошибка: введите число")

del_L = L0 * alpha * (t2 - t1)
L = L0 + del_L

if del_L < 0.1:
    expansion = "Пренебрежимое"
elif del_L <= 2:
    expansion = "Учитываемое"
else:
    expansion = "Значительное"

print("\nРезультаты расчёта:")
print("Материал:", material)
print("Коэффициент расширения:", alpha)
print("Изменение длины:", round(del_L, 4), "мм")
print("Конечная длина:", round(L, 4), "мм")
print("Класс расширения:", expansion)