#!/usr/bin/python

"""
Node Definitions

Xiaowen Wang
"""


class NodeBase(object):
    """
    Node Base Class
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data

    def __str__(self):
        return "(%s, %s)" % (self.key, self.data)

    def __repr__(self):
        return "<Node key:%s data:%s>" % (self.key, self.data)


class BinaryNode(NodeBase):
    """
    Binary Tree Node
    """

    def __init__(self, key, data=None):
        super(BinaryNode, self).__init__(key, data)
        self.left = None
        self.right = None


class HeapNode(NodeBase):
    """
    Heap Node
    """


if __name__ == "__main__":

    n0 = BinaryNode(1)
    print n0

    n1 = BinaryNode(2, 10)
    print n1

    exit(0)
