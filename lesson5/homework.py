"""
1. Создать функцию которая создает список
натуральных чисел от минимума до максимума с шагом
"""


def custom_range(a, b=0, c=1):
    _list = []
    if a > b:
        a, b = b, a
    while a < b:
        _list.append(a)
        a += c
    return _list


"""
2. Написать функцию такую что
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""


def accum(_list):
    _list_new = ""
    count = 1
    for i in _list:
        i *= count
        i = i.title()
        _list_new += i + "-"
        count += 1
    return _list_new[0:-1]


"""
3. Our football team finished the championship.
The result of each match look like "x:y".
Results of all matches are recorded in the array.
For example: ["3:1", "2:2", "0:1", ...]
Write a function that takes such list and counts
the points of our team in the championship.
Rules for counting points for each match:
if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:
there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""


def points(_list):
    count = 0
    for i in _list:
        x, y = int(i[0]), int(i[2])
        if x > y:
            count += 3
        elif x < y:
            pass
        else:
            count += 1
    return count


"""
4. Написать функцию, которая
определяет в списке наиболее встречаемое значение.
Вернуть значение и количество повторений.
"""


def max_number_count(_list):
    _dict = {}
    for a in _list:
        try:
            _dict[a] += 1
        except KeyError:
            _dict[a] = 1
    max_amount = 0
    position = 0
    for i in _dict:
        if _dict[i] > max_amount:
            max_amount = _dict[i]
            position = i
    return position, max_amount


if __name__ == '__main__':
    assert custom_range(1, 4) == [1, 2, 3]
    assert custom_range(1, 4, 2) == [1, 3]
    assert custom_range(1, 1, 2) == []
    assert custom_range(5) == [0, 1, 2, 3, 4]
    print('custom_range - OK')

    assert accum("abcd") == "A-Bb-Ccc-Dddd"
    assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    assert accum("cwAt") == "C-Ww-Aaa-Tttt"
    print('accum - OK')

    assert points(
        ['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2',
         '4:3']) == 30
    assert points(
        ['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4',
         '4:4']) == 10
    assert points(
        ['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4',
         '3:4']) == 0
    assert points(
        ['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4',
         '3:4']) == 15
    assert points(
        ['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4',
         '3:4']) == 12
    print('points - ok')

    assert max_number_count([1, 2, 2, 3, 3, 3]) == (3, 3)
    assert max_number_count([1, 2, 3, 1, 1]) == (1, 3)
    print('max_number_count - OK')
