s = input("Введите строку: ")

while (s.count("(") != 1 or
       s.count(")") != 1 or
       s.index("(") > s.index(")")):
    print("Ошибка! Введите строку с правильными скобками")
    s = input("Введите строку: ")

start = s.index("(")
end = s.index(")")

print("Символы внутри скобок:", s[start + 1:end])