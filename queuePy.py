"""
Filename : queuePy
Author : Archit Joshi
Description : Implementing queue datastructure using python list (FIFO)
Language : python3
"""


class Queue:
    """
    Implementing the queue datastructure from scratch using lists.
    """

    def __init__(self):
        """
        Instantiate empty queue using list.
        """
        self.queue = []

    def isEmpty(self):
        """
        Check if the queue is empty.

        :return: True if the list/queue is empty
        """
        return len(self.queue) == 0

    def enqueue(self, data):
        """
        Insert data into queue.

        :param data: data
        :return: None
        """
        self.queue.append(data)

    def dequeue(self):
        """
        Delete item from the front of queue (the first element in the list)
        :return: None if the queue is empty
        """
        if self.isEmpty():
            return None
        self.queue.remove(0)

    def size(self):
        """
        Return length of queue
        :return: length of queue
        """
        return len(self.queue)

    def isFront(self):
        """
        Return the element in the front of the queue.

        :return: first element in the list
        """
        if self.isEmpty():
            return None
        return self.queue[0]
