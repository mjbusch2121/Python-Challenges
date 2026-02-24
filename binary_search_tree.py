# binary search tree in python

class Node:
    def __init__(self, key):
        self.key = key # value of the node
        self.left = None # reference to the left child node
        self.right = None # reference to the right child node

class BinarySearchTree:
    def __init__(self):
        self.root = None # reference to the root node of the BST

    def insert(self, key):
        if self.root is None: # if the tree is empty
            self.root = Node(key) # create a new node and set it as the root
        else:
            self._insert_recursive(self.root, key) # call the recursive insert function with the root

    def _insert_recursive(self, node, key): 
        if key < node.key: # if the key is less than the current node's key
            if node.left is None: # if the left child is empty
                node.left = Node(key) # create a new node and set it as left child
            else:
                self._insert_recursive(node.left, key) # recursively insert in the left subtree
        else:
            if node.right is None: # if the right child is empty
                node.right = Node(key) # create a new node and set it as right child
            else:
                self._insert_recursive(node.right, key) # recursively insert in the right subtree

    def search(self, key):
        return self._search_recursive(self.root, key) # call the recursive search function with the root
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key: # if the node is None or the key is found
            return node # return the node(found) or none (not found)
        if key < node.key: # if the key is less than the current node's key
            return self._search_recursive(node.left, key) # recursively search in the left subtree
        else:
            return self._search_recursive(node.right, key) # recursively search in the right subtree

# test
# using produce points as values

bst = BinarySearchTree() # create a new bst project

# insert nodes
for price in [50,30,70,20,40,60,80]:
    bst.insert(price)

found = bst.search(40)
print("Found:" , found.key if found else "Not found")

missing = bst.search(99)
print("Found:", missing.key if missing else "Not found")