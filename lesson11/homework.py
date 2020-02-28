"""
1.
Напишите итератор Fibonacci(n), который генерирует числа Фибоначчи до
n включительно.
"""


# Генерирует числа Фибоначчи до какого-то числа
class Fibonacci:
    def __init__(self, amount):
        self.counter = 0
        self.amount = amount
        self.current = 1
        self.previous = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.amount:
            raise StopIteration
        else:
            current = self.current
            self.current += self.previous
            self.previous = current
            return current


# Генерирует числа Фибоначчи до n-го числа
class FibonacciNumber(Fibonacci):
    def __next__(self):
        if self.counter >= self.amount:
            raise StopIteration
        else:
            self.counter += 1
            current = self.current
            self.current += self.previous
            self.previous = current
            return current


# print("1й итератор", end=": ")
# counter = Fibonacci(7)
# for i in counter:
#     print(i, end=" ")

# print("\n2й итератор", end=": ")
# counter1 = FibonacciNumber(7)
# for a in counter1:
#     print(a, end=" ")

"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""


class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.current:
            raise StopIteration
        else:
            current = self.current
            self.current += 2
            return current


# counter = EvenNumbers(13)
# for i in counter:
#     print(i)

"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


class Factorials:
    def __init__(self, n):
        self.nMax = n + 1  # Для генерации до n включительно
        self.current = 1
        self.nNow = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nNow >= self.nMax:
            raise StopIteration
        else:
            current = self.current
            self.current *= self.nNow
            self.nNow += 1
            return current


# factor = Factorials(6)
# for i in factor:
#     print(i, end=" ")

"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


# Насколько я понял задание нужно чтобы
# выводилось что-то вроде Треугольника Паскаля:
#     1       1
#    1 1      1 1
#   1 2 1     1 2 1
#  1 3 3 1    1 3 3 1
# 1 4 6 4 1   1 4 6 4 1

class BinomialCoefficients:
    def __init__(self, n):
        self.nMax = n + 1
        self.nNow = 1
        self.previous = [1]
        self.current = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.nNow >= self.nMax:
            raise StopIteration
        elif self.nMax <= 1:
            raise StopIteration
        else:
            if self.nNow == 1:
                self.nNow += 1
                return self.previous

            self.current = [1]
            for elem in range(len(self.previous) - 1):
                summa = self.previous[elem] + self.previous[elem + 1]
                self.current.append(summa)
            self.current.append(1)

            self.nNow += 1
            current = self.current
            self.previous = self.current
            return current


# x = 12
# binom = BinomialCoefficients(x)
# for i in binom:
#     difference = x - len(i)
#     print(" " * difference, end="")
#     print(i)
