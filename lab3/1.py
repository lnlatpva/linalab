total_population = 0
total_area = 0
for i in range (1, 13):
    print('Район №', i)
    population = float(input('Введите кол-во жителей (тыс. чел.):'))
    area = float(input('Введите площадь района (км2):'))
    total_population += population
    total_area += area
density = total_population / total_area
print('Средняя плотность населения:', density)