"""
DSC 20 Final Project Utility File

Please copy and paste your Stack and Queue implementation from Lab 10.
"""


class Collection:
    """
    A class to abstract the common functionalities of Stack and Queue.
    This class should not be initialized directly.
    """

    def __init__(self):
        """ Constructor. """
        self.items = []
        self.num_items = 0

    def size(self):
        """ Get the number of items stored. """
        return self.num_items

    def is_empty(self):
        """ Check whether the collection is empty. """
        if self.size()==0:
            return True
        else:
            return False

    def clear(self):
        """ Remove all items in the collection. """
        self.items = []


class Stack(Collection):
    """
    Stack class.
    """

    def push(self, item):
        """ Push `item` to the stack. """
        if item == None:
            raise ValueError('item cannot be None')
        self.num_items +=1
        self.items.append(item)

    def pop(self):
        """ Pop the top item from the stack. """
        self.num_items -=1
        if self.size() == 0:
            return None
        removed = self.items.pop()
        return removed

    def peek(self):
        """ Peek the top item. """
        if self.size():
            return self.items[-1]
        return None

    def __str__(self):
        """ Return the string representation of the stack. """
        if self.num_items == 0:
            return "(bottom) (top)"
        elif self.num_items == 1:
            return "(bottom) {} (top)".format(self.items[0])
        else:
            return "(bottom) {} (top)".format(' -- '.join([str(i) \
            for i in self.items]))


class Queue(Collection):
    """
    Queue class.
    """

    def enqueue(self, item):
        """ Enqueue `item` to the queue. """
        if item == None:
            raise ValueError('item cannot be None')
        self.num_items +=1
        self.items.append(item)

    def dequeue(self):
        """ Dequeue the front item from the queue. """
        self.num_items -=1
        if self.size() == 0:
            return None
        removed = self.items[0]
        del self.items[0]
        return removed

    def peek(self):
        """ Peek the front item. """
        if self.size():
            return self.items[0]
        return None

    def __str__(self):
        """ Return the string representation of the queue. """
        if self.num_items == 0:
            return "(front) (rear)"
        elif self.num_items == 1:
            return "(front) {} (rear)".format(self.items[0])
        else:
            return "(front) {} (rear)".format(' -- '.join([str(i) \
            for i in self.items]))
