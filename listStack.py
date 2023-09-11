"""
Filename : listStack.py
Author : Archit Joshi
Description : Implementing stack datastructure using list (LIFO)
Language : python3
"""


class Stack:
    """
    Class to implement a stack using a list.
    """

    def __init__(self):
        """
        Instantiate empty list as a stack
        """
        self.stack = []

    def isEmpty(self):
        """
        Check if the stack is empty.
        :return: True iff the stack is empty
        """
        return len(self.stack) == 0

    def push(self, data):
        """
        Insert data into stack.

        :param data: data to be inserted
        :return: None
        """
        self.stack.append(data)

    def pop(self):
        """
        Remove the element at the top of the stack (last element in a list)

        :return: None iff the stack is already empty
        """
        if self.isEmpty():
            return None
        self.stack.pop()

    def peek(self):
        """
        Return the element at the top of the stack (last element in a list)

        :return: element at the top of stack
        """
        if self.isEmpty():
            return None
        return self.stack[-1]

    def clear(self):
        """
        Clear out the stack.
        :return: None
        """
        if self.isEmpty():
            return None
        self.stack.clear()
