# todo: Преобразуйте переменную age и foo в число

age = "23"
foo = "23abc"

age = int(age)
foo = int(foo[:2]) #Срезаем только числа


# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)


# Преобразуйте переменную flag в Boolean
flag = 1

flag = bool(flag)


# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

str_one = bool(str_one)
str_two = bool(str_two)

# Преобразуйте значение 0 и 1 в Boolean

zero = bool(0)
one = bool(1)


# Преобразуйте False в строку

end = str(False)
