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
        By using BFS, make a mark when for the first time encountering a non-full node
        """
        if self._root is None:
            return True

        # create a queue with root in
        queue = []
        queue.append(self._root)

        # this will clip when for the fist time a non-full node is found
        non_full_node_found = False

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left:
                # Exit point:
                # if a non-full node has been found before,
                # this node should not have any child
                if non_full_node_found:
                    return False

                queue.append(node.left)

            else:
                non_full_node_found = True

            if node.right:
                # Eixt point:
                # if a non-full node has been found before,
                # this node should not have any right child
                if non_full_node_found:
                    return False

                queue.append(node.right)

            else:
                non_full_node_found = True

        # If the tree can be traversed, then it is complete
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

    def _get_node_path(self, parent, node, path):
        """
        Internal path search method
        """
        if parent is None:
            return False

        path.append(parent)

        if node is parent:
            return True

        if self._get_node_path(parent.left, node, path):
            return True

        elif self._get_node_path(parent.right, node, path):
            return True

        else:
            path.pop()
            return False

    def get_node_path(self, node):
        """
        Return a node path (list) to a certain node from root
        """
        if self._root is None:
            return []

        if node is self._root:
            return [self._root]

        path = []

        if self._get_node_path(self._root, node, path):
            return path
        else:
            return []

    def get_node_parent(self, node):
        """
        Return a node's parent
        """
        if self._root is None:
            return None

        path = self.get_node_path(node)
        if len(path) >= 2:
            # the one before last node is the perent
            return path[-2]
        else:
            return None

    def get_nearest_common_parent(self, node1, node2):
        """
        Return the nearst common parent of two given nodes
        """
        if self._root is None:
            return None

        if node1 is None or node2 is None:
            return None

        path1 = self.get_node_path(node1)
        if not path1:
            return None

        path2 = self.get_node_path(node2)
        if not path2:
            return None

        ret_node = None

        # If both two nodes can be found in the tree,
        # then find the first different path node
        while len(path1) and len(path2):
            t_node1 = path1.pop(0)
            t_node2 = path2.pop(0)

            if t_node1.data == t_node2.data:
                ret_node = t_node1
                continue
            else:
                return ret_node

        return ret_node

    def get_distance(self, node1, node2):
        """
        Return the distance between two nodes
        """
        if self._root is None:
            return None

        if node1 is None or node2 is None:
            return None

        path1 = self.get_node_path(node1)
        if not path1:
            return None

        path2 = self.get_node_path(node2)
        if not path2:
            return None

        # remove the common path
        while len(path1) and len(path2):
            if path1[0].data == path2[0].data:
                path1.pop(0)
                path2.pop(0)
            else:
                break

        # the distance is the sum of those remaining path nodes
        return len(path1) + len(path2)

    def get_max_distance(self):
        """
        Return the max distance between two nodes in the tree
        """
        if self._root is None:
            return 0

        max_l = 0
        max_r = 0

        if self._root.left:
            max_l = self._get_max_depth(self._root.left)

        if self._root.right:
            max_r = self._get_max_depth(self._root.right)

        return max_l + max_r


if __name__ == "__main__":

    # Create a BST
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Traverse the BST
    bst.print_inorder()
    bst.print_preorder()
    bst.print_postorder()
    bst.print_level_order()

    # Validate the BST
    print "Is the BST valid? %s" % bst.is_valid()
    print "Is the BST balanced? %s" % bst.is_balanced()
    print "Is the BST full? %s" % bst.is_full()
    print "The BST node num: %s" % bst.get_num_of_node()
    print "The BST leaf node num: %s" % bst.get_num_of_leaf_node()
    print "The BST depth: %s" % bst.get_max_depth()

    # Perform a search in the BST
    search_target = 20
    target_node = bst.lookup(search_target)
    if target_node:
        print "Node %s is found in the BST" % target_node
    else:
        print "Node %s is NOT found in the BST" % target_node

    # Remove root node 50
    print "Removing root node (50)..."
    bst.delete(50)
    bst.print_inorder()
    bst.print_level_order()

    print "Is the BST valid? %s" % bst.is_valid()
    print "Is the BST balanced? %s" % bst.is_balanced()
    print "Is the BST full? %s" % bst.is_full()
    print "The BST node num: %s" % bst.get_num_of_node()
    print "The BST leaf node num: %s" % bst.get_num_of_leaf_node()
    print "The BST depth: %s" % bst.get_max_depth()

#     pth = bst.get_node_path(bst.get_root())
#     if len(pth) > 0:
#         print [n.data for n in pth]
#
#     pth = bst.get_node_path(target_node)
#     if len(pth) > 0:
#         print [n.data for n in pth]
#
#     print bst.get_nearest_common_parent(bst.get_root(), target_node).data
#     print bst.get_distance(bst.get_root(), target_node)
#     print bst.get_max_distance()

    # target_node = Node(100)
    # path = bst.get_node_path(target_node)
    # print path

    # bst.delete(11);
    # bst.traverse_inorder()
#     print bst.is_valid()
#     print bst.get_num_of_node()
#     print bst.get_num_of_leaf_node()
#     print bst.get_num_of_node_with_level(4)
#     print bst.get_max_depth()
#     print bst.is_balanced()
#     print bst.is_complete()
#     print bst.is_full()

    exit(0)