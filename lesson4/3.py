# Заполнить список вещественных чисел вводом с клавиатуры.
# Найте элементы списка, которые меньше среднего арифметического.

spisok = []             # Для всех чисел
spisok_min = []         # Для чисел меньше среднего
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

srednee_arifmetick = 0

for i in range(len(spisok)):
    srednee_arifmetick += spisok[i]

srednee_arifmetick /= len(spisok)

for i in range(len(spisok)):
    if spisok[i] < srednee_arifmetick:
        spisok_min.append(spisok[i])

print("Для списка: " + str(spisok))
print("Элементы, которые меньше среднего арифметического:")
print(spisok_min)
