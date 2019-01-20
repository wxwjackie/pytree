#!/usr/bin/python

"""
BST example

Xiaowen Wang
"""

import sys

from node import Node


class BST(object):
    """
    Binary Searching Tree
    """

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def _insert(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, data)
                return node.left
            else:
                return self._insert(node.left, key, data)
        else:
            if node.right is None:
                node.right = Node(key, data)
                return node.right
            else:
                return self._insert(node.right, key, data)

    def insert(self, key, data=None):
        """
        Insert a node to the tree
        """
        if self._root is None:
            self._root = Node(key, data)
            return self._root
        else:
            return self._insert(self._root, key, data)

    def _inorder(self, node):
        if node is None:
            return

        self._inorder(node.left)
        sys.stdout.write(str(node) + ' ')
        self._inorder(node.right)

    def print_inorder(self):
        """
        Print the tree in an in-order manner
        """
        if self._root is None:
            print "The BST is empty"
            return

        print "The current BST (in-order) is:"
        self._inorder(self._root)
        sys.stdout.write('\n')
        sys.stdout.flush()

    def _preorder(self, node):
        if node is None:
            return

        sys.stdout.write(str(node) + ' ')
        self._preorder(node.left)
        self._preorder(node.right)

    def print_preorder(self):
        """
        print the tree in a pre-order manner
        """
        if self._root is None:
            print "The BST is empty"
            return

        print "The current BST (pre-order) is:"
        self._preorder(self._root)
        sys.stdout.write('\n')
        sys.stdout.flush()

    def _postorder(self, node):
        if node is None:
            return

        self._postorder(node.left)
        self._postorder(node.right)
        sys.stdout.write(str(node) + ' ')

    def print_postorder(self):
        """
        Print the tree in a post-order manner
        """
        if self._root is None:
            print "The BST is empty"
            return

        print "The current BST (post-order) is:"
        self._postorder(self._root)
        sys.stdout.write('\n')
        sys.stdout.flush()

    def print_level_order(self):
        """
        Breadth first search
        """
        if self._root is None:
            print "The BST is empty"
            return

        # init a queue with root
        queue = [self._root]

        print "The current BST (level-order) is:"

        while len(queue) > 0:
            # print and pop the front of queue
            node = queue.pop(0)
            sys.stdout.write(str(node) + ' ')

            # enqueue the left child
            if node.left:
                queue.append(node.left)

            # enqueue the right child
            if node.right:
                queue.append(node.right)

        sys.stdout.write('\n')
        sys.stdout.flush()

    def _lookup(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._lookup(node.left, key)
        else:
            return self._lookup(node.right, key)

    def lookup(self, key):
        """
        Search a data in the tree
        """
        return self._lookup(self._root, key)

    def _delete_node_with_child(self, node, child=None, parent=None):
        """
        To delete the node with one or zero child
        """
        if parent:
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child
        else:
            self._root = child

        # Release the current node from memory
        node.left = None
        node.right = None
        node.key = None
        node.data = None
        del node

    @staticmethod
    def _find_min_node(node, parent=None):
        """
        Find the node with min key from the subtree
        """
        cur_node = node
        cur_parent = parent
        while cur_node.left:
            cur_parent = cur_node
            cur_node = cur_node.left
        return cur_node, cur_parent

    def _delete(self, node, key, parent=None):
        if node is None:
            return

        if key < node.key:
            self._delete(node.left, key, parent=node)

        elif key > node.key:
            self._delete(node.right, key, parent=node)

        else:
            # Found the node to delete, there are 3 cases to deal with.
            if node.left and node.right:
                # If the node has both two children,
                successor, successor_parent = self._find_min_node(node.right, parent=node)
                node.key = successor.key
                node.data = successor.data
                self._delete(successor, successor.key, successor_parent)

            elif node.left:
                # If the node only has one left child,
                # copy the left child to the node,
                # and delete the node.
                self._delete_node_with_child(node, child=node.left, parent=parent)

            elif node.right:
                # If the node only has one right child,
                # copy the right child to the node,
                # and delete the node.
                self._delete_node_with_child(node, child=node.right, parent=parent)

            else:
                # If the node is a leaf, simply remove it from the tree.
                self._delete_node_with_child(node, parent=parent)

    def delete(self, key):
        """
        Remove a node from the tree
        """
        self._delete(self._root, key)

    def _is_valid(self, node, min_val, max_val):
        if node is None:
            return True

        if node.key < min_val or node.key > max_val:
            return False

        return (self._is_valid(node.left, min_val, node.key - 1) and
                self._is_valid(node.right, node.key + 1, max_val))

    def is_valid(self):
        """
        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search tree.
        """
        return self._is_valid(self._root, -sys.maxint - 1, sys.maxint)

    def _get_num_of_node(self, node):
        if node is None:
            return 0

        return 1 + (self._get_num_of_node(node.left) +
                    self._get_num_of_node(node.right))

    def get_num_of_node(self):
        """
        Return the number of node in the tree
        """
        return self._get_num_of_node(self._root)

    def _get_num_of_leaf_node(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return (self._get_num_of_leaf_node(node.left) +
                self._get_num_of_leaf_node(node.right))

    def get_num_of_leaf_node(self):
        """
        Return the number of leaf node in the tree
        """
        return self._get_num_of_leaf_node(self._root)

    def _get_num_of_node_with_level(self, node, k):
        if node is None or k < 1:
            return 0

        if k == 1:
            return 1

        return (self._get_num_of_node_with_level(node.left, k - 1) +
                self._get_num_of_node_with_level(node.right, k - 1))

    def get_num_of_node_with_level(self, k):
        """
        Return the number of node in the level k.
        """
        return self._get_num_of_node_with_level(self._root, k)

    def _get_max_depth(self, node):
        if node is None:
            return 0

        return 1 + max(self._get_max_depth(node.left),
                       self._get_max_depth(node.right))

    def get_max_depth(self):
        """
        Return the depth of tree
        """
        return self._get_max_depth(self._root)

    def _get_balance(self, node):
        """
        Return the balance of node
        """
        if node is None:
            return 0

        # balance is left max depth - right max depth
        return abs(self._get_max_depth(node.left) -
                   self._get_max_depth(node.right))

    def _is_balanced(self, node):
        if node is None:
            return True

        if (self._get_balance(node) <= 1 and
            self._is_balanced(node.left) and
            self._is_balanced(node.right)):
            return True

        return False

    def is_balanced(self):
        """
        The height difference between left and right subtree should be less than 1;
        The left subtree is balanced;
        The right subtree is balanced;
        """
        return self._is_balanced(self._root)

    def is_complete(self):
        """
        A complete binary tree is a binary tree in which every level,
        except possibly the last, is completely filled,
        and all nodes are as far left as possible.
        """
        # Create a queue with root in
        queue = [self._root] if self._root is not None else []

        # By using breadth first traverse,
        # mark down when the first non-full node is met.
        non_full_node_found = False

        while len(queue) > 0:
            # Every time remove a parent node from the queue.
            node = queue.pop(0)

            if node.left:
                if non_full_node_found:
                    # If a non-full node has been found before,
                    # this node should not have any left child.
                    return False
                else:
                    # Otherwise continue to enqueue the left child.
                    queue.append(node.left)

            else:
                # Found the non-full node if no left child.
                non_full_node_found = True

            if node.right:
                if non_full_node_found:
                    # If a non-full node has been found before,
                    # this node should not have any right child.
                    return False
                else:
                    # Otherwise continue to enqueue the right child.
                    queue.append(node.right)

            else:
                # Found the non-full node if no right child.
                non_full_node_found = True

        # If the tree can be traversed by this BFT, then it is complete
        return True

    def _is_full(self, node):
        if node is None:
            return True

        # If no child, it is OK
        if node.left is None and node.right is None:
            return True

        # If there is only one child, it is not OK
        if node.left is None or node.right is None:
            return False

        return self._is_full(node.left) and self._is_full(node.right)

    def is_full(self):
        """
        A full binary tree is a tree in which every node
        other than the leaves has two children.
        """
        return self._is_full(self._root)

    def is_perfect(self):
        """
        A Binary tree is Perfect Binary Tree in which all internal nodes
        have two children and all leaves are at same level.
        A perfect binary tree of height (h) has (2^h-1) nodes
        """
        h = self._get_max_depth(self._root)
        num = self._get_num_of_node(self._root)
        return (num == (2 ** h - 1))

    def _get_node_path(self, parent, node, path):
        # If there is no more parent to the target node
        # in this branch, just return.
        if parent is None:
            return False

        # Then keep track of this parent node.
        path.append(parent)

        # If target node is found, return positive.
        if node is parent:
            return True

        # If not, continue to search the left side of subtree.
        if self._get_node_path(parent.left, node, path):
            return True

        # If not, continue to search the right side of subtree.
        if self._get_node_path(parent.right, node, path):
            return True

        # If the target node cannot be found from both sides of subtree,
        # remove the current parent node from the path record.
        path.pop()
        return False

    def get_node_path(self, node):
        """
        Return the node path list to the given node from root
        """
        path = []
        if node is not None:
            self._get_node_path(self._root, node, path)
        return path

    def get_node_parent(self, node):
        """
        Return the parent node of the given node.
        """
        path = self.get_node_path(node)
        if len(path) >= 2:
            # The one before last node is the parent node.
            return path[-2]
        return None

    def get_nearest_common_parent(self, node1, node2):
        """
        Return the nearest common parent of the two given nodes.
        """
        if self._root is None:
            return None

        if node1 is None or node2 is None:
            return None

        # Get the path of node 1
        path1 = self.get_node_path(node1)
        if not path1:
            return None

        # Get the path of node 2
        path2 = self.get_node_path(node2)
        if not path2:
            return None

        common_parent = None

        # If both two nodes can be found in the tree,
        # the go through the two paths to find the last common element,
        # which is the nearest common parent.
        for n1, n2 in zip(path1, path2):
            if n1 is n2:
                common_parent = n1
                continue
            else:
                break

        return common_parent

    def get_distance(self, node1, node2):
        """
        Return the distance between the two given nodes
        """
        if self._root is None:
            return -1

        if node1 is None or node2 is None:
            return -1

        path1 = self.get_node_path(node1)
        if not path1:
            return -1

        path2 = self.get_node_path(node2)
        if not path2:
            return -1

        i = 0

        # The distance between two nodes is to count the different nodes
        # in both paths list.
        for n1, n2 in zip(path1, path2):
            if n1 is not n2:
                break
            i += 1

        dist1 = 0 if i >= len(path1) else len(path1[i:])
        dist2 = 0 if i >= len(path2) else len(path2[i:])
        return dist1 + dist2

    def get_max_distance(self):
        """
        Return the distance between the two farthest nodes in the tree
        """
        if self._root is None:
            return -1

        # The max breadth is the sum of the max depth of
        # its left subtree and its right subtree.
        return (self._get_max_depth(self._root.left) +
                self._get_max_depth(self._root.right))

    def get_min_node(self):
        """
        Return the node with minimum key value
        """
        current = self._root

        # Traverse the node from root to leftmost until the leaf.
        # That leaf node is the node with minimum key value.
        while current.left is not None:
            current = current.left

        return current

    def get_max_node(self):
        """
        Return the node with maximum key value
        """
        current = self._root

        # Traverse the node from root to rightmost until the leaf.
        # That leaf node is the node with maximum key value.
        while current.right is not None:
            current = current.right

        return current


def traverse_helper(bst):
    bst.print_inorder()
    bst.print_preorder()
    bst.print_postorder()
    bst.print_level_order()


def show_attr_helper(bst):
    print "Is the BST valid?      %s" % bst.is_valid()
    print "Is the BST balanced?   %s" % bst.is_balanced()
    print "Is the BST full?       %s" % bst.is_full()
    print "Is the BST complete?   %s" % bst.is_complete()
    print "Is the BST perfect?    %s" % bst.is_perfect()
    print "The BST node num:      %s" % bst.get_num_of_node()
    print "The BST leaf node num: %s" % bst.get_num_of_leaf_node()
    print "The BST max depth:     %s" % bst.get_max_depth()
    print "The BST max breadth:   %s" % bst.get_max_distance()
    print "The BST min node:      %s" % bst.get_min_node()
    print "The BST max node:      %s" % bst.get_max_node()


if __name__ == "__main__":

    print "Creating a BST..."
    bst = BST()
    print "Inserting node (50)..."
    bst.insert(50)
    print "Inserting node (30)..."
    bst.insert(30)
    print "Inserting node (20)..."
    bst.insert(20)
    print "Inserting node (40)..."
    bst.insert(40)
    print "Inserting node (70)..."
    bst.insert(70)
    print "Inserting node (60)..."
    bst.insert(60)
    print "Inserting node (80)..."
    bst.insert(80)

    traverse_helper(bst)
    show_attr_helper(bst)

    target_key = 20
    target_node = bst.lookup(target_key)
    if target_node:
        print "Node %s is found in the BST" % target_node
    else:
        print "Node %s is NOT found in the BST" % target_node

    print "Removing node (50)..."
    bst.delete(50)
    print "Removing node (20)..."
    bst.delete(20)

    traverse_helper(bst)
    show_attr_helper(bst)

    print "Inserting node (100)..."
    node_100 = bst.insert(100)
    print "Inserting node (35)..."
    node_35 = bst.insert(35)

    node_100_path = bst.get_node_path(node_100)
    print "Node (100) path: %s" % node_100_path
    node_35_path = bst.get_node_path(node_35)
    print "Node (35) path:  %s" % node_35_path

    parent_35_100 = bst.get_nearest_common_parent(node_100, node_35)
    print "The nearest common parent of node (100 & 35): %s" % parent_35_100

    dist_35_100 = bst.get_distance(node_100, node_35)
    print "The distance between node (100 & 35): %s" % dist_35_100

    node_unknown = Node(500)
    node_unknown_path = bst.get_node_path(node_unknown)
    print "Node (unknown) path: %s" % node_unknown_path

    print "The parent of node (100): %s" % bst.get_node_parent(node_100)

    exit(0)
