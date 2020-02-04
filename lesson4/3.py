# Заполнить список вещественных чисел вводом с клавиатуры.
# Найте элементы списка, которые меньше среднего арифметического.

spisok = []             # Для всех чисел
spisok_min = []         # Для чисел меньше среднего
print("Введите числа, когда закончите нажмите Enter.")

while True:
    a = input()
    if a == "":
        break
    else:
        try:
            spisok.append(float(a))
        except ValueError:
            print("Вводите только числа!")

srednee_arifmetick = 0

for item in spisok:
    srednee_arifmetick += item

srednee_arifmetick /= len(spisok)

for i in spisok:
    if i < srednee_arifmetick:
        spisok_min.append(i)

print("Для списка: " + str(spisok))
print("Элементы, которые меньше среднего арифметического:")
print(spisok_min)
