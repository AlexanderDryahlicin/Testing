"""
Нужно реализовать класс Stack со следующими методами:
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")  # Явное сообщение об ошибке
        return self.items.pop()  # Удаляет и возвращает последний элемент за один шаг

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)



c = Stack()
c.push(1)
c.push(2)
c.push(3)
print(c.pop())
print(c.size())

"""
Используя стек из задания 1, решите задачу на проверку сбалансированности скобок.
 Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий 
 ему закрывающий, и пары скобок правильно вложены друг в друга.
"""


def is_balanced(brackets):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in brackets:
        if char in pairs.values(): #если открывающая
            stack.push(char)
        elif char in pairs.keys(): #если закрывающая
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


print(is_balanced("()"))  # True
print(is_balanced("({[]})"))  # True
print(is_balanced("(]"))  # False
print(is_balanced("([)]"))  # False
print(is_balanced("{"))  # False