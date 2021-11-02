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
    def add_node(self, node_data):
        def node_placement(pointer, node_data):
            if node_data is None:
                return Node(node_data)
            elif node_data > pointer.root:
                pointer.right = node_placement(pointer.right, node_data)
            else:
                pointer.left = node_placement(pointer.left, node_data)
            return pointer      
        self.root = node_placement(self.root, node_data)
    # """insert left function"""
    # def insert_left(self, new_node):
    #     if self.left_child is None:
    #         self.left_child = BinarySearchTree(new_node)
    #     else:
    #         new_child = BinarySearchTree(new_node)
    #         new_child.left_child = self.left_child
    #         self.left_child = new_child
    # """insert right function"""    
    # def insert_right(self, new_node):
    #     if self.right_child == None:
    #         self.right_child = BinarySearchTree(new_node)
    #     else:
    #         new_child = BinarySearchTree(new_node)
    #         new_child.right_child = self.right_child
    #         self.right_child = new_child
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
    def in_order(self):

        def node_placement(pointer, node_list):
            if pointer is None:
                return
            if pointer.left:
                node_placement(pointer.left, node_list)
            node_list.append(pointer.data)
            if pointer.right:
                node_placement(pointer.right, node_list)
        node_list = []
        node_placement(self.root, node_list)
        return node_list
# myNode1 = Node(10)
# myNode2 = Node(2)
# myNode3 = Node(15)
# myNode4 = Node(5)

# myTree = BinarySearchTree(myNode1)
# print(myTree)