"""
1*. Переписать код из homework6 используя ООП
2. Реализовать класс "очередь"
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
- в качестве инициализации принимает размер очереди, если параметр не указан,
то очередь - бесконечная
- выдать сообщение об ошибке, если в полную очередь добавить элемент нельзя,
или из пустой очереди достать элемент
3. Реализовать класс "стек"
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
- в качестве инициализации принимает размер стека, если параметр не указан,
то стек - бесконечный
- выдать сообщение об ошибке, если в полный стек добавить элемент нельзя,
или из пустого стека достать элемент
"""


# Реализовка класса "очередь"


class Turn:

    def __init__(self, amount=None):
        self.amount = amount
        self.counter = 0
        self.turn = []

    def in_turn(self, unit):
        if self.counter == self.amount and self.amount is not None:
            raise Exception("Очередь полная")
        else:
            self.turn.append(unit)
            self.counter += 1

    def out_turn(self):
        if self.counter == 0:
            raise Exception("Пустая очередь")
        self.turn.pop(0)
        self.counter -= 1


museum = Turn()

museum.in_turn("Наша Таня")
museum.in_turn("Громко плачет")
museum.in_turn("Уронила")
museum.in_turn("в речку мячик")
print(museum.turn)
museum.out_turn()
museum.out_turn()
museum.out_turn()
museum.out_turn()
museum.out_turn()


# Реализовка класса "стек"


class Stack:

    def __init__(self, amount=None):
        self.stack = []
        self.amount = amount
        self.counter = 0

    def in_stack(self, unit):
        if self.amount == self.counter and self.amount is not None:
            raise Exception("Полная очередь")
        self.stack.append(unit)
        self.counter += 1

    def out_stack(self):
        if self.counter == 0:
            raise Exception("Пустая очередь")
        else:
            self.stack.pop()
            self.counter -= 1


museum = Stack()

museum.in_stack("Наша Таня")
museum.in_stack("Громко Плачет")
museum.in_stack("Уронила")
museum.in_stack("в речку мячик")
print(museum.stack)
museum.out_stack()
museum.out_stack()
museum.out_stack()
museum.out_stack()
museum.out_stack()
