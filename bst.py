"""Binary search tree"""
# from main import Pair
class BinarySearchTree:
    """init function"""
    def __init__(self, root_obj = None):
        self.root = root_obj
        # self.left_child = None
        # self.right_child = None
    def add(self, node):
        self.root = self.add_helper(node, self.root)
    def add_helper(self, node, current_node):
        """Add function"""
        if current_node is None:
            return node
        else:
            if current_node.letter == node.letter:
                current_node.count += 1
                return current_node
            elif current_node.letter < node.letter:
                current_node.right_child = self.add_helper(node, node.right_child)
            else:
                current_node.left_child = self.add_helper(node, node.left_child)

        return current_node
    def height(self, node):
        """Height function"""
        if node is None:
            return -1
        else:
            left_depth = self.height(node.left_child)
            right_depth = self.height(node.right_child)

            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
    def size(self, node=None):
        """Size function"""
        if node is None:
            return 0
        else:
            return (self.size(node.left_child)+ 1 + self.size(node.right_child))

    def find(self, node, letter):
        """Find function"""
        if node is None or node.letter == letter:
            return node
        if node.letter < letter:
            return self.find(node.right_child, letter)
        return self.find(node.left_child, letter)
    def get_root_val(self):
        """Get root value function"""
        return self.root
    def set_root_val(self, new_obj):
        """Set root value function"""
        self.root = new_obj
    # def get_left_child(self, node):
    #     """Get Left child function"""
    #     return node.left_child
    # def get_right_child(self, node):
    #     """Get Right child function"""
    #     return node.right_child
    def is_empty(self):
        """Is Empty function"""
        if self.root is None:
            return True
        else:
            return False
    def in_order(self):
        self.in_order_helper(self.root)
    def in_order_helper(self, node):
        """In Order function"""
        if node:
            self.in_order(node.left_child)
            print(node)
            self.in_order(node.right_child)
    def pre_order(self):
        """Preorder function"""
        if self.root:
            print(self.root)
            self.pre_order(self.root.left_child)
            self.pre_order(self.root.right_child)
    def post_order(self, node):
        """Postorder function"""
        if node.letter:
            print(node)
            self.post_order(node.left_child)
            self.post_order(node.right_child)
        # def node_placement(pointer, node_list):
        #     if pointer is None:
        #         return
        #     if pointer.left:
        #         node_placement(pointer.left, node_list)
        #     node_list.append(pointer.data)
        #     if pointer.right:
        #         node_placement(pointer.right, node_list)
        # node_list = []
        # node_placement(self.root, node_list)
        # return node_list
# myNode1 = Node(10)
# myNode2 = Node(2)
# myNode3 = Node(15)
# myNode4 = Node(5)

# myTree = BinarySearchTree(myNode1)
# print(myTree)
