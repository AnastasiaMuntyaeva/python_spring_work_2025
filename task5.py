#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

a = int(input('Введите число: '))
b = int(input('Введите число: '))

# Сумма чисел
total = a+b
print(f"Сумма чисел {a} и {b} составляет: {total}")

# Разность чисел
if a > b:
    residual = a - b
else:
    residual = b - a
print(f"Разность чисел {a} и {b} составляет: {residual}")

# Частное чисел
if a > b:
    quotient = a/b
else:
    quotient = b/a
print(f"Частное чисел {a} и {b} составляет: {quotient}")

# Произведение чисел
product = a*b
print(f"Произведение чисел {a} и {b} составляет: {product}")

# Результат целочисленного деления
if a > b:
    quotient_int = a//b
else:
    quotient_int = b//a
print(f"Частное чисел {a} и {b} составляет: {quotient_int}")

# Результат деления с остатком
if a > b:
    remainder = a % b
else:
    remainder = b % a
print(f"Частное чисел {a} и {b} составляет: {remainder}")

# Результат возведение в степень
exponentiation_1 = a**b
exponentiation_2 = b**a
print(f"Возведение {a} в степень {b} составляет: {exponentiation_1}")
print(f"Возведение {b} в степень {a} составляет: {exponentiation_2}")