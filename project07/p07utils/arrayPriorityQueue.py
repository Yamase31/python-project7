"""
File: arrayPriorityQueue.py
Author: Harry Pinkerton, James Lawson
Project: 7


"""

from .node import Node
from .arrayQueue import ArrayQueue

class ArrayPriorityQueue(ArrayQueue):
    """A link-based priority queue implementation."""

    # Constructor 
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)

    # Mutator methods
    def add(self, item):
        """Inserts"""
        if len(self._items) == len(self):
            self.grow()

        newIndex = len(self)

        for i in range(len(self)):
            if item <= self._items[i]:
                newIndex = i
                break
            
        for j in range(len(self), newIndex, -1):
            self._items[j] = self._items[j -1]
        self._items[newIndex] = item
        self._size += 1
        super().incModCount()
