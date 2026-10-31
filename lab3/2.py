gift = float(input())
age = int(input())
limit = float(input())
while gift <= limit:
    gift += 1
    gift = gift * 2 + age
print('Подарок превысит заданную сумму на', age, 'день рождения')
print('Размер подарка:', gift, 'долларов')