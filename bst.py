"""Node class"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""Binary search tree"""
class BinarySearchTree:
    """init function"""
    def __init__(self, root_obj = None):
        self.key = root_obj
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
        return self.key
    """Set root value function"""
    def set_root_val(self, new_obj):
        self.key = new_obj
    """Get Left child function"""
    def get_left_child(self):
        return self.left_child
    """Get Right child function"""
    def get_right_child(self):
        return self.right_child
    def size(self):
        if self is None:
            return 0
    # def is_empty(self):
    #     if self is None:
    #         self = 0
    #         return self