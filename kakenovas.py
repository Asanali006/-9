from fractions import Fraction

numerator1 = int(input("Введите числитель первой дроби: "))
denominator1 = int(input("Введите знаменатель первой дроби: "))
numerator2 = int(input("Введите числитель второй дроби: "))
denominator2 = int(input("Введите знаменатель второй дроби: "))

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

sum_result = fraction1 + fraction2
multiply_result = fraction1 * fraction2

print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {multiply_result}")