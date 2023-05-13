"""
In computer science, a stack is a linear data structure that follows a particular order in which operations are performed.
The order may be LIFO (Last In First Out) where the last item that was put in the stack is the first one to be removed.

Your task is to implement a basic stack in Python with the following methods:

push(item): Add an item to the top of the stack.
pop(): Remove and return the top item from the stack. If the stack is empty, raise an exception with the message "Stack is empty".
peek(): Return the top item from the stack without removing it. If the stack is empty, return None.
is_empty(): Return True if the stack is empty, False otherwise.

"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0


# TestCase

def test_stack():
    s = Stack()

    # Test that stack is initially empty
    assert s.is_empty() == True

    # Test push and peek
    s.push(1)
    assert s.peek() == 1

    # Test multiple pushes and peek
    s.push(2)
    assert s.peek() == 2
    s.push(3)
    assert s.peek() == 3

    # Test pop
    assert s.pop() == 3
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.peek() == 1

    # Test pop on empty stack
    try:
        s.pop()
        s.pop()
    except IndexError as e:
        assert str(e) == "Stack is Empty"

    # Test peek on empty stack
    assert s.peek() == None
    assert s.is_empty() == True

test_stack()
