# Заполнить список вещественных чисел вводом с клавиатуры.
# Сколько элементов списка больше по модулю максимального числа.

_list = []             # Для всех чисел
list_big = []         # Для чисел больших махимального
print("Введите числа, когда закончите нажмите Enter.")

while True:
    try:
        a = input()
        if a == "":
            break
        else:
            _list.append(float(a))
    except ValueError:
        print("Вводите только числа!")

max_unit = float(0)
for item in _list:
    if max_unit < item:
        max_unit = item

for i in _list:
    if abs(i) > max_unit:
        list_big.append(i)

print("Для списка " + str(_list))
print("Элементов списка больше по модулю максимального числа: "
      + str(len(list_big)))
