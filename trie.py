#!/usr/bin/python


class TrieNode(object):
    """
    A node class for trie tree
    """
    def __init__(self):
        self.children = {}  # Dict to hold children nodes
        self.is_end = False
        # self.data = None

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


class Trie(object):
    """
    A Trie Tree
    """
    def __init__(self):
        self._root = TrieNode()

    def insert(self, key):
        """
        Insert a key to the trie tree
        """
        # From the root
        p = self._root

        # If the character is already existing, move next;
        # otherwise create a new one and move on.
        for ch in key:
            if not ch in p.children:
                p.children[ch] = TrieNode()

            p = p.children[ch]

        # until the last one, and mark it the end.
        p.is_end = True

    def search(self, key):
        """
        Search a key in trie tree
        """
        p = self._root

        for ch in key:
            if not ch in p.children:
                return False

            p = p.children[ch]

        return p.is_end

    def delete(self, key):
        """
        Delete a key from trie tree.
        1. No key, nothing happens;
        2. Key in a standalone path, just delete the path;
        3. Key is part of other keys, just unmark the node;
        4. Other keys are prefix of the key, delete until the longest other key.
        """
        l = len(key)

        if l > 0:
            self._delete(self._root, key, 0, l)

    def _delete(self, node, key, i, l):
        """
        Recursive innner deletion
        """
        if node:
            # Base case: reach the last character
            if i == l:
                # Mark the node not the end anymore
                node.is_end = False
                # If the node is a leaf, we need to delete it.
                if node.is_leaf():
                    return True
                # else the node is being shared, cannot delete it.
                return False

            else:
                # Recursively crawl down the tree
                if self._delete(node.children.get(key[i], None), key, i+1, l):
                    # Delete the child if it is a leaf
                    # and not the end for other keys.
                    del node.children[key[i]]
                    # Climb up
                    # Checking the current node can be deleted or not.
                    return node.is_free()

        # Key not found case
        return False

    def _display(self, node, key_str):
        """
        """
        if node.is_end:
            print key_str

        for ch in node.children:
            key_str += ch
            self._display(node.children[ch], key_str)
            key_str = key_str[:-1]

    def display(self):
        """
        Traverse the tree for all keys (depth first)
        """
        print "Trie Content:"

        if not self._root.is_leaf():
            self._display(self._root, "")

        print "*" * 15


if __name__ == '__main__':

    t = Trie()
    t.display()

    t.insert("abc")
    t.insert("abe")
    t.insert("ab")
    t.display()

    print t.search("abc")
    print t.search("abe")
    print t.search("ab")

    t.delete("abc")
    t.delete("ab")

    print t.search("abc")
    print t.search("abe")
    print t.search("ab")

    t.display()

    exit(0)
