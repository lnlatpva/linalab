s = input("Введите строку:")
a = s.find('(')
b = s.find(')')
print(s[a + 1:b])