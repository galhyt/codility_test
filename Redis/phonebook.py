"""
Phonebook quesiton  1. Suggest a datastructure for implementing a basic phonebook functinoality with    three operations:    * Add an entry.    * Get an entry - returns a phone number in case the given name exists in the phonebook.    * delete an entry - deletes an entry with a given name if exists. 2. We need a new operation added: search - given a prefix of a name, return all entries with keys matching that prefix.    How will the data structure above change to support the searching functionality?






"""
from typing import List, Dict, Any


class TreeNode:
    def __init__(self, val:str = None, children: Dict[str, Any] = None):
        self.val = val
        self.children = children


class Phonebook:
    def __init__(self):
        self.phones = TreeNode()

    def add(self, name, number):
        letters = name.split('')
        node = self.phones
        for l in letters:
            if l not in node.children:
                node.children[l] = TreeNode()
            node = node.children[l]

        node.val = number

    def get(self, name):
        pass

    def delete(self, name):
        letters = name.split('')
        node = self.phones
        nodes_letters = []
        parent = None
        for l in letters:
            if l not in node.children:
                return False
            nodes_letters.append((l, parent))
            parent = node
            node = node.children[l]

        del_candidate = node
        while del_candidate:
            if del_candidate.children:
                del_candidate.val = None
                return True

            parent, l = nodes_letters.pop(0)
            parent.children.pop(l)

            del_candidate = parent

    def search(self, prefix):
        letters = prefix.split('')
        node = self.phones
        for l in letters:
            if l not in node.children:
                return []
            node = node.children[l]

        entries = {}
        arr = [(node, prefix)]
        while arr:
            node, name = arr.pop(0)
            if node.val:
                entries[name] = node.val
            arr += [(c, name+l) for l, c in node.children.items()]

        return entries





