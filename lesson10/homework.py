"""
0. (*) Написать функцию, которая из списка чисел составляет
максимальное число
[98, 9, 34] -> 99834
"""


def max_number(_list):
    pass


"""
1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с
несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""


"""
2.
Напишите менеджер контекста Timer, который позволяет получать текущее время
выполнения кода (отсчет начинается с конструкции with):
with Timer("Time: {}") as timer:
    do_some_logic()
    print(timer.now())  # Time: 3.4123 sec
    do_some_other_logic()
    print(timer.now())  # Time: 5.71 sec
"""

import time


class Timer:
    def __init__(self, item):
        self.start = 0
        self.text = item

    def __enter__(self):
        self.start = time.time()
        return self

    def now(self):
        return self.text.format(f"{time.time() - self.start} sec")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# if __name__ == '__main__':
#     assert max_number([234, 123, 98]) == 98234123
#     assert max_number([1, 2, 3, 4]) == 4321
#     assert max_number([]) is None
#     assert max_number([98, 9, 34]) == 99834
#     print('max_number - OK')
