"""
DSC 20 Lab 10
Name: Zehui Zhang
PID:  A16151490
"""


# Question 1.1
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


# Question 1.2
class Stack(Collection):
    """
    Stack class.

    >>> stk = Stack()
    >>> stk.size()
    0
    >>> stk.is_empty()
    True
    >>> str(stk)
    '(bottom) (top)'
    >>> stk.push(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> stk.push('LAB 10')
    >>> stk.size()
    1
    >>> stk.is_empty()
    False
    >>> stk.push('DSC')
    >>> stk.push(20)
    >>> stk.size()
    3
    >>> str(stk)
    '(bottom) LAB 10 -- DSC -- 20 (top)'
    >>> stk.pop()
    20
    >>> stk.pop()
    'DSC'
    >>> stk.peek()
    'LAB 10'
    >>> stk.size()
    1
    >>> stk.clear()
    >>> stk.pop()
    >>> stk.peek()
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
        if self.size() == 0:
            return None
        else:
            return self.items[-1]

    def __str__(self):
        """ Return the string representation of the stack. """
        if self.num_items == 0:
            return "(bottom) (top)"
        elif self.num_items == 1:
            return "(bottom) {} (top)".format(self.items[0])
        else:
            return "(bottom) {} (top)".format(' -- '.join([str(i) \
            for i in self.items]))


# Question 1.3
class Queue(Collection):
    """
    Queue class.

    >>> que = Queue()
    >>> que.size()
    0
    >>> que.is_empty()
    True
    >>> str(que)
    '(front) (rear)'
    >>> que.enqueue(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> que.enqueue('LAB 10')
    >>> que.size()
    1
    >>> que.is_empty()
    False
    >>> que.enqueue('DSC')
    >>> que.enqueue(20)
    >>> que.size()
    3
    >>> str(que)
    '(front) LAB 10 -- DSC -- 20 (rear)'
    >>> que.dequeue()
    'LAB 10'
    >>> que.dequeue()
    'DSC'
    >>> que.peek()
    20
    >>> que.size()
    1
    >>> que.clear()
    >>> que.dequeue()
    >>> que.peek()
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
        if self.size() == 0:
            return None
        else:
            return self.items[0]

    def __str__(self):
        """ Return the string representation of the queue. """
        if self.num_items == 0:
            return "(front) (rear)"
        elif self.num_items == 1:
            return "(front) {} (rear)".format(self.items[0])
        else:
            return "(front) {} (rear)".format(' -- '.join([str(i) \
            for i in self.items]))

# Question 2
def parentheses_checker(expression):
    """
    A function that checks whether all parentheses `{}, [], ()`
    are balanced in the given `expression`.

    >>> parentheses_checker("(((]})")
    False
    >>> parentheses_checker("(")
    False
    >>> parentheses_checker("(){}[]]")
    False
    >>> parentheses_checker("(   x   )")
    True
    >>> parentheses_checker("a()b{}c[]d")
    True
    >>> parentheses_checker("")
    True
    """
    my_stack = Stack()
    open = ['(','[','{']
    close = [')',']','}']
    my_dic = {'(':')','[':']','{':'}'}
    for i in expression:
        if i in open:
            my_stack.push(i)
        elif i in close:
            ele = my_stack.peek()
            if ele == None:
                return False
            else:
                if i == my_dic[ele]:
                    my_stack.pop()
    if my_stack.size() == 0:
        return True
    else:
        return False


# Question 3
def inf_skip_increasing(iterable):
    """
    A generator that takes in an `iterable` object and infinitely yields its
    items. This generator skips items by an increasing amount after each
    yield. If this generator reached the end of the `iterable`, proceed from
    the front.

    >>> gen = inf_skip_increasing(range(10))
    >>> next(gen)
    0
    >>> next(gen)
    1
    >>> [next(gen) for _ in range(10)]
    [3, 6, 0, 5, 1, 8, 6, 5, 5, 6]
    """
    my_queue = Queue()
    skip = 0
    while True:
        while my_queue.size() < skip+1:
            for i in iterable:
                my_queue.enqueue(i)
        yield my_queue.dequeue()
        for j in range(skip):
            my_queue.dequeue()
        skip += 1
