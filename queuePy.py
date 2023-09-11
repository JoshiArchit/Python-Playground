"""
Filename :
Author : Archit Joshi
Description : Implementing queue datastructure using python list (FIFO)
Language : python3
"""


class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            return None
        self.queue.remove(0)

    def size(self):
        return len(self.queue)

    def isFront(self):
        if self.isEmpty():
            return None
        return self.queue[0]
