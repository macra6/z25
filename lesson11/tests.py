import unittest
from homework import *


class HomeworkTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(list(Fibonacci(7)), [1, 1, 2, 3, 5])
        self.assertEqual(list(FibonacciNumber(7)), [1, 1, 2, 3, 5, 8, 13])

    def test_EvenNumbers(self):
        self.assertEqual(list(EvenNumbers(13)), [0, 2, 4, 6, 8, 10, 12])

    def test_Factorials(self):
        self.assertEqual(list(Factorials(6)), [1, 1, 2, 6, 24, 120])

    def test_BinomialCoefficients(self):
        self.assertEqual(list(BinomialCoefficients(5)), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])


if __name__ == '__main__':
    unittest.main()
