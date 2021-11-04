from main import Pair

"""Binary search tree"""
class BinarySearchTree:
    """init function"""
    def __init__(self, root_obj = None):
        self.root = root_obj
        self.left_child = None
        self.right_child = None
    """Add function"""
    def add(self, letter):
        if letter is None:
            Pair(letter).count += 1
            return Pair(letter)
        else:
            if self.root.letter == letter:
                return self.root
            elif self.root < letter:
                self.root.right = self.add(self.root.right, letter)
            else:
                self.root.left = self.add(self.root.left, letter)

        return self.root
    """Height function"""
    def height(self, node):
        if node is None:
            return -1
        else:
            left_depth = self.height(node.left_child)
            right_depth = self.height(node.right_child)

            if (left_depth > right_depth):
                return left_depth + 1
            else:
                return right_depth + 1
    """Size function"""
    def size(self, node):
        if node is None:
            return 0 
        else:
            return (self.size(node.left_child)+ 1 + self.size(node.right_child))

    """Find function"""
    def find(self, current_node, letter):
        if current_node is None or self.root.letter == letter:
            return current_node
        if self.root.letter < letter:
            return self.find(self.root.right, letter)
        return self.find(self.root.left, letter)
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