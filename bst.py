"""Node class"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
"""Binary search tree"""
class BinarySearchTree:
    """init function"""
    def __init__(self, root_obj = None):
        self.root = root_obj
        self.left_child = None
        self.right_child = None
    """insert left function"""
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinarySearchTree(new_node)
        else:
            new_child = BinarySearchTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child
    """insert right function"""    
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinarySearchTree(new_node)
        else:
            new_child = BinarySearchTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child
    """Get root value function"""
    def get_root_val(self):
        return self.root
    """Set root value function"""
    def set_root_val(self, new_obj):
        self.root = new_obj
    """Get Left child function"""
    def get_left_child(self):
        return self.left_child
    """Get Right child function"""
    def get_right_child(self):
        return self.right_child
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    
node = Node(10)
# node.left = Node(5)
# node.right = Node(12)
print(node)
# myTree = BinarySearchTree(node)
# print(myTree.is_empty())