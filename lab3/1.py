total_people = 0
total_area = 0

for i in range(12):
    print("Район", i + 1)

    people = -1
    while people < 0:
        try:
            people = float(input("Население (тыс. чел.): "))
            if people < 0:
                print("Население не может быть отрицательным")
        except ValueError:
            print("Введите число")
            people = -1

    area = 0
    while area <= 0:
        try:
            area = float(input("Площадь (км2): "))
            if area <= 0:
                print("Площадь должна быть больше нуля")
        except ValueError:
            print("Введите число")
            area = 0

    total_people += people * 1000
    total_area += area

density = total_people / total_area

print("Средняя плотность:", round(density, 2), "чел/км2")