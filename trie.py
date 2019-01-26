#!/usr/bin/python

"""
Trie Operations

Xiaowen Wang
"""

from node import TrieNode


class Trie(object):
    """
    Trie Tree
    """

    def __init__(self):
        self._root = TrieNode()

    def insert(self, key, data=None):
        """
        Insert a key with data to trie.
        """
        assert isinstance(key, str)

        node = self._root

        # If the character is already existing, move next;
        # otherwise create a new one and move on.
        for ch in key:
            if not ch in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        # Until the last one, and mark it the end and save the data
        node.is_end = True
        node.data = data

    def search(self, key):
        """
        Search a key from trie, return the trie node.
        """
        assert isinstance(key, str)

        node = self._root

        # Traverse trie for each character in the key,
        # if any character not found, just return none.
        for ch in key:
            if not ch in node.children:
                return None

            node = node.children[ch]

        # Here the end of key is reached, and check if it is a key end.
        # If not, just return none.
        if not node.is_end:
            return None

        # The key-end is found, return the node.
        return node

    def _delete(self, node, key, i, l):
        if node:
            # Base case: reach the last character.
            if i == l:
                # Mark the node is not the end anymore.
                node.is_end = False
                # If the node is a leaf, it is save to delete it.
                if node.is_leaf():
                    return True
                # else the node is being shared with other keys,
                # it cannot be deleted yet.
                return False

            else:
                # Recursively crawl down the tree.
                if self._delete(node.children.get(key[i], None), key, i + 1, l):
                    # Delete the child node if it is a leaf.
                    del node.children[key[i]]
                    # Climb up and check if the current node can be deleted.
                    return node.is_free()

        # Key not found in trie.
        return False

    def delete(self, key):
        """
        Delete a key from trie tree.
        1. No key, nothing happens;
        2. Key in a standalone path, just delete the path;
        3. Key is part of other keys, just unmark the node;
        4. Other keys are prefix of the key, delete until the longest other key.
        """
        assert isinstance(key, str)

        l = len(key)
        if l > 0:
            self._delete(self._root, key, 0, l)

    def _display(self, node, key_path):
        # If the node is a key-end, print out the key and its value.
        if node.is_end:
            print "%s: %s" % (key_path, node.data)

        # Then go through all the children node recursively.
        for ch in node.children:
            # Add the current character to the key path
            key_path += ch
            # Recursive depth first traversal to the child
            self._display(node.children[ch], key_path)
            # Finished one child traversal, climb up one step,
            # remove the last character from key path for another child traversal.
            key_path = key_path[:-1]

    def display(self):
        """
        Traverse the tree for all keys (depth first)
        """
        print "The trie content:"

        if not self._root.is_leaf():
            self._display(self._root, '')


if __name__ == '__main__':

    print "Creating trie..."
    t = Trie()

    print "Inserting (abc: 1)..."
    t.insert("abc", data=1)
    print "Inserting (abe: 2)..."
    t.insert("abe", data=2)
    print "Inserting (ab: 3)..."
    t.insert("ab", data=3)

    t.display()

    print "Search <abc>: %s" % t.search("abc")
    print "Search <abe>: %s" % t.search("abe")
    print "Search <ab> : %s" % t.search("ab")

    print "Deleting <abc>..."
    t.delete("abc")
    print "Deleting <ab>..."
    t.delete("ab")

    print "Search <abc>: %s" % t.search("abc")
    print "Search <abe>: %s" % t.search("abe")
    print "Search <ab> : %s" % t.search("ab")

    t.display()

    exit(0)
