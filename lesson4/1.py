# Вводятся два целых числа.
# Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть)
# и частное (в любом случае).

while True:
    try:
        number1 = int(input("Введите 1-е число"))
        number2 = int(input("Введите 2-е число"))
    except ValueError:
        print("Пожалуйста, вводите только целые числа")
    else:
        break

if number2 == 0:
    print("Второе число должно быть не 0 (делить на 0 нельзя)")
elif number1 % number2 == 0:
    print(str(number1) + " делиться на " + str(number2) + " без остатка:")
    print(str(number1) + " / " + str(number2) + " = " + str(number1//number2))
else:
    print(str(number1) + " делиться на " + str(number2) + " c остатком:")
    print(str(number1) + " / " + str(number2) + " = " + str(number1//number2))
    print("Остаток от деления = " + str(number1 % number2))
