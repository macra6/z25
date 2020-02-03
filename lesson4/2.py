# Заполнить список вещественных чисел вводом с клавиатуры.
# Сколько элементов списка больше по модулю максимального числа.

spisok = []             # Для всех чисел
spisok_big = []         # Для чисел больших махимального
print("Введите числа, когда закончите нажмите Enter.")

while True:
    try:
        a = input()
        if a == "":
            break
        else:
            spisok.append(float(a))
    except ValueError:
        print("Вводите только числа!")

max_unit = float(0)

for i in range(len(spisok)):
    if max_unit < spisok[i]:
        max_unit = spisok[i]

for i in range(len(spisok)):
    if abs(spisok[i]) > max_unit:
        spisok_big.append(spisok[i])

print("Для списка " + str(spisok))
print("Элементов списка больше по модулю максимального числа: "
      + str(len(spisok_big)))
