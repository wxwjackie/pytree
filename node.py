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

    def is_leaf(self):
        return self.left is None and self.right is None


class HeapNode(NodeBase):
    """
    Binary Heap Node
    """


class TrieNode(object):
    """
    Trie Tree Node
    """

    def __init__(self):
        self.children = {}  # Points to children nodes
        self.is_end = False  # Is the end of a word/key?
        self.data = None  # Can store some extra content

    def is_leaf(self):
        """
        True if the node is a leaf.
        A leaf node has no any children.
        """
        return not self.children

    def is_free(self):
        """
        True if the node is free to be deleted.
        A free node should be a leaf and not marked as the end of key.
        """
        return self.is_leaf() and not self.is_end


if __name__ == "__main__":

    n0 = BinaryNode(1)
    print n0

    n1 = BinaryNode(2, 10)
    print n1

    exit(0)
