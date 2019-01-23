#!/usr/bin/python

"""
Binary Heap

Xiaowen Wang
"""

import sys


class HeapNode(object):
    """
    Heap Node
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data


class MinHeap(object):
    """
    Min Heap:
    In a Min Binary Heap, the key at root must be minimum among all keys
    present in Binary Heap. The same property must be recursively true
    for all nodes in Binary Tree.
    """

    def __init__(self):
        self._vec = []

    @property
    def size(self):
        return len(self._vec)

    @staticmethod
    def _p_idx(i):
        """
        Return the parent index
        """
        assert i > 0
        return (i - 1) / 2

    @staticmethod
    def _l_idx(i):
        """
        Return the left child index
        """
        assert i >= 0
        return 2 * i + 1

    @staticmethod
    def _r_idx(i):
        """
        Return the right child index
        """
        assert i >= 0
        return 2 * i + 2

    def display(self):
        print "Min Heap: %s" % [n.key for n in self._vec]

    def get_root(self):
        return self._vec[0]

    def get_min_node(self):
        return self._vec[0]

    def _perc_up(self, i):
        """
        Percolate the item up.
        It is a bottom-up process to swap the new node with its parent,
        if the parent's key is greater.
        """
        while i > 0 and self._vec[self._p_idx(i)].key > self._vec[i].key:
            self._vec[self._p_idx(i)], self._vec[i] = \
                self._vec[i], self._vec[self._p_idx(i)]
            i = self._p_idx(i)

    def _perc_down(self, i):
        """
        Percolate the item down.
        It is also called heapify-down.
        It finds the smallest of its children if there is any,
        and swap them repeatedly until it gets to the correct position.
        """
        smallest = i
        l = self._l_idx(i)
        r = self._r_idx(i)

        # Find the smallest child node
        if l < self.size and self._vec[l].key < self._vec[smallest].key:
            smallest = l
        if r < self.size and self._vec[r].key < self._vec[smallest].key:
            smallest = r

        if smallest != i:
            # Swap the current node with the smallest child node
            self._vec[i], self._vec[smallest] = self._vec[smallest], self._vec[i]
            # Recursively heapify the subtree
            self._perc_down(smallest)

    def extract_min(self):
        """
        Remove the minimum node, which is the first one in the list.
        """
        if self.size == 0:
            return

        if self.size == 1:
            self._vec.pop()
            return

        # Copy the last node to the root, remove the last node,
        # and heapify the whole tree from root.
        self._vec[0] = self._vec[-1]
        self._vec.pop()
        self._perc_down(0)

    def insert(self, key, data=None):
        """
        Insert a new node
        """
        node = HeapNode(key, data)

        # First put the new node to the end
        self._vec.append(node)

        # Get the new node index
        i = self.size - 1

        # Fix the broken part until it satisfies the rule
        self._perc_up(i)

    def remove(self, i):
        """
        Delete the i-th node
        """
        assert self.size > i

        # Assign the smallest int to the ith node
        self._vec[i].key = -sys.maxint - 1

        # Fix the broken part until it satisfies the rule
        # By the end, the to-be-deleted node will be at the root
        self._perc_up(i)

        # At last, remove the root.
        self.extract_min()


if __name__ == "__main__":

    print "Creating MinHeap..."
    mh = MinHeap()

    print "Inserting node (1)..."
    mh.insert(1)
    print "Inserting node (3)..."
    mh.insert(3)
    print "Inserting node (6)..."
    mh.insert(6)
    print "Inserting node (5)..."
    mh.insert(5)
    print "Inserting node (9)..."
    mh.insert(9)
    print "Inserting node (8)..."
    mh.insert(8)
    print "Inserting node (2)..."
    mh.insert(2)

    mh.display()

    print "Removing the 2-th node..."
    mh.remove(2)

    mh.display()

    print "Remove the min node..."
    mh.extract_min()

    mh.display()

    exit(0)
