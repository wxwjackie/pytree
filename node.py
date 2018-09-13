#!/usr/bin/python

"""
Node definition

Xiaowen Wang
"""


class Node(object):
    """
    Tree node structure
    """
    def __init__(self, data):
        """
        Constructor to create a node
        """
        self.left = None
        self.right = None
        self.data = data
