# create a tree and store in an array

# initialize the tree as a list
tree = [1,2,3,4,5,6,7]

# function to insert a node in the tree
def left_child(i):
    return 2 * i + 1
def right_child(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

# print the tree
print("Root:", tree[0])
print("Left child of root:", tree[left_child(0)])
print("Right child of root:", tree[right_child(0)])
print("Parent of index 4:", tree[parent(4)])

# visually this represents:
#         1         (index 0)
#        / \
#       2   3       (index 1, 2)
#      / \ / \
#     4  5 6  7     (index 3, 4, 5, 6)