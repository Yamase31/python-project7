"""
File: arrayQueue.py
Author: Harry Pinkerton, James Lawson
Project: 7

"""

from .arrays import Array
from .abstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = -1
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # Same as an iterator for an arrayBag, only using modulo inside self._items access
        #  to wrap the cursor around the end of the array
        myModCount = self._modCount
        cursor = 0

        while cursor < len(self):
            yield self._items[(cursor + self._front) % len(self._items)]
            if myModCount != self._modCount:
                raise AttributeError("Cannot modify!")
            cursor += 1
        

    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise ValueError("Attempt to peek at empty queue")
        return self._front

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._front = self._rear = None
        pass
        
    
    def grow(self):
        tempArray = Array(len(self) * 2)
        for i in range(len(self)):
            tempArray[i] = self._items[i]
        self._items = tempArray
        pass

    def shrink(self):
        # Only shrink if we're not too small
        if len(self) // 2 > ArrayQueue.DEFAULT_CAPACITY:
            pass
        
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if self.isEmpty():
            self._front = self._rear = 0
        else:
            self._rear += 1
            self._rear %= len(self._items)

        self._items[self._rear] = item
        self._size += 1
        

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        data = self._items[self._front]
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear = -1
        else:
            self._front += 1
            self._front %= len(self._items)
        return data

        
         
