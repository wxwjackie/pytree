#!/usr/bin/python

"""
AVL (Adelson, Velski & Landis) Tree is height balancing binary search tree.
AVL tree checks the height of the left and the right sub-trees,
and assures that the difference is not more than 1.

Xiaowen Wang
"""

from bst import BST


class AVL(BST):
    """
    AVL Tree
    """

    def _rotate_right(self, node):
        """
        Right rotation
        """
        parent = self.get_parent(node)
        is_right_child = False

        if parent:
            if node is parent.right:
                is_right_child = True

        new_p = node.left
        node.left = new_p.right
        new_p.right = node

        if parent:
            if is_right_child:
                parent.right = new_p
            else:
                parent.left = new_p
        else:
            self._root = new_p

    def _rotate_left(self, node):
        """
        Left rotation
        """
        parent = self.get_parent(node)
        is_left_child = False

        if parent:
            if node is parent.left:
                is_left_child = True

        # right child becomes new parent
        new_p = node.right
        # deal with the left child of previously right child
        node.right = new_p.left
        # the current node becomes left child
        new_p.left = node

        if parent:
            if is_left_child:
                parent.left = new_p
            else:
                parent.right = new_p
        else:
            self._root = new_p

    def _balance_node(self, node):
        """
        Balance the subtree from the given node
        """
        # get the balance of given node
        bal = self._get_balance(node)

        # heavily-left subtree needs right rotation
        if bal > 1:
            # in case the left child has more right offsprings
            # then needs left rotation first
            if self._get_balance(node.left) < 0:
                self._rotate_left(node.left)
            self._rotate_right(node)

        # heavily-right subtree needs left rotation
        if bal < -1:
            # in case the right child has more left offspring,
            # then needs right rotation first
            if self._get_balance(node.right) > 0:
                self._rotate_right(node.right)
            self._rotate_left(node)

    def insert(self, key, data=None):
        """
        Override
        Insert a node to the tree, still keeping balanced
        """
        # get new node
        new_node = super(AVL, self).insert(key, data)

        if new_node is self._root:
            return self._root
        else:
            node = new_node
            # balance the new tree from the new node to root
            while node:
                self._balance_node(node)
                node = self.get_parent(node)

        return new_node

    def _delete(self, node, key, parent=None):
        """
        Internal delete method
        """
        if node is None:
            # No such node storing given data
            return

        if key < node.key:
            self._delete(node.left, key, parent=node)

        elif key > node.key:
            self._delete(node.right, key, parent=node)

        else:
            # Found the node
            if node.left and node.right:
                # The node has both two chilren
                successor, successor_p = self._find_min_node(node.right, parent=node)
                node.key = successor.key
                node.data = successor.data
                self._delete(successor, successor.key, successor_p)

            elif node.left:
                # The node only has one left child
                self._delete_node_with_child(node, child=node.left, parent=parent)
                # then balance the parent
                if parent:
                    self._balance_node(parent)

            elif node.right:
                # The node only has one right child
                self._delete_node_with_child(node, child=node.right, parent=parent)
                # then balance the parent
                if parent:
                    self._balance_node(parent)

            else:
                # The node is a leaf
                self._delete_node_with_child(node, parent=parent)
                # then check the parent's balance
                if parent:
                    self._balance_node(parent)


if __name__ == "__main__":

    avl = AVL()

    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    avl.insert(20)
    avl.traverse_preorder()
    avl.traverse_inorder()
    avl.traverse_postorder()
    avl.traverse_level_order()

    search_target = 20
    target_node = avl.lookup(search_target)
    if target_node:
        print "%s is found in the AVL tree" % search_target
    else:
        print "%s is NOT found in the AVL tree" % search_target

    path = avl.get_node_path(avl.get_root())
    if len(path) > 0:
        print [node.key for node in path]

    path = avl.get_node_path(target_node)
    if len(path) > 0:
        print [node.key for node in path]

    print avl.get_nearest_common_parent(avl.get_root(), target_node).key
    print avl.get_distance(avl.get_root(), target_node)
    print avl.get_max_distance()

    # target_node = Node(100)
    # path = avl.get_node_path(target_node)
    # print path

    # avl.delete(11);
    # avl.traverse_inorder()
    print avl.is_valid()
    print avl.get_num_of_node()
    print avl.get_num_of_leaf_node()
    print avl.get_num_of_node_with_level(4)
    print avl.get_max_depth()
    print avl.is_balanced()
    print avl.is_complete()
    print avl.is_full()

    exit(0)

