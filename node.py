#!/usr/bin/python

"""
Node definition

Xiaowen Wang
"""


class Node(object):
    """
    Tree node structure
    """

    def __init__(self, key, data=None):
        """
        Constructor to create a node
        """
        self.left = None
        self.right = None
        self.key = key
        self.data = data

    def __str__(self):
        return "(%s, %s)" % (self.key, self.data)

    def __repr__(self):
        return "<Node key:%s data:%s>" % (self.key, self.data)


if __name__ == "__main__":

    n0 = Node(1)
    print n0

    n1 = Node(2, 10)
    print n1

    exit(0)
