#!/usr/bin/python

import sys


class HeapNode(object):
    """
    Node for binary heap
    """

    def __init__(self, key, val=None):
        self._key = key
        self._val = val

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def value(self):
        return self._val

    @value.setter
    def value(self, val):
        self._val = val


class MinHeap(object):
    """
    Binary heap class
    """

    def __init__(self):
        self._vec = []

    @property
    def size(self):
        return len(self._vec)

    @staticmethod
    def _parent_index(i):
        return (i - 1) / 2

    @staticmethod
    def _left_index(i):
        return 2 * i + 1

    @staticmethod
    def _right_index(i):
        return 2 * i + 2

    def insert(self, node):
        """
        Insert a node
        """
        # First put the new node to the end
        self._vec.append(node)
        i = self.size - 1

        # Fix the broken part until it satisfies the rule
        self._reorder(i)

    def remove(self, i):
        """
        Delete ith node
        """
        # Assign the smallest int to the ith node
        self._vec[i].key = -sys.maxint - 1

        # Fix the broken part until it satisfies the rule
        # By the end, the to-be-deleted node will be at the root
        self._reorder(i)

        # Put the last node to the root
        # and heapify the whole tree
        self._vec[0] = self._vec[-1]
        self._vec.pop()
        self._heapify(0)

    def _reorder(self, i):
        while i != 0 and self._vec[self._parent_index(i)].key > self._vec[i].key:
            self._vec[self._parent_index(i)], self._vec[i] = self._vec[i], self._vec[self._parent_index(i)]
            i = self._parent_index(i)

    def _heapify(self, i):
        smallest = i
        l = self._left_index(i)
        r = self._right_index(i)

        # Find the smallest child node
        if l < self.size and self._vec[l].key < self._vec[smallest].key:
            smallest = l
        if r < self.size and self._vec[r].key < self._vec[smallest].key:
            smallest = r

        if smallest != i:
            # Swap the current node with the smallest child node
            self._vec[i], self._vec[smallest] = self._vec[smallest], self._vec[i]
            # Recursively heapify the subtree
            self._heapify(smallest)

    def display(self):
        print([n.key for n in self._vec])


if __name__ == "__main__":

    mh = MinHeap()

    mh.insert(HeapNode(1))
    mh.insert(HeapNode(3))
    mh.insert(HeapNode(6))
    mh.insert(HeapNode(5))
    mh.insert(HeapNode(9))
    mh.insert(HeapNode(8))

    mh.display()

    n = mh.remove(0)

    mh.display()

    exit(0)
