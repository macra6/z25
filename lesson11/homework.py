"""
1.
Напишите итератор Fibonacci(n), который генерирует числа Фибоначчи до
n включительно.
"""


# Генерирует числа Фибоначчи до какого-то числа
class Fibonacci():
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

print("1й итератор", end=": ")
counter = Fibonacci(7)
for i in counter:
    print(i, end=" ")

print("\n2й итератор", end=": ")
counter1 = FibonacciNumber(7)
for a in counter1:
    print(a, end=" ")

"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""

"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""
