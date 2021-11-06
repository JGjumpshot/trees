"""Binary search tree"""
# from main import Pair
class BinarySearchTree:
    """init function"""
    def __init__(self, root_obj = None):
        self.root = root_obj
        self._size = 0
        # self.left_child = None
        # self.right_child = None
    def add(self, node):
        self.root = self.add_helper(node, self.root)
    def add_helper(self, node, current_node, parent=None):
        """Add function"""
        if current_node is None:
            self._size += 1
            node.parent = parent
            return node
        else:
            if current_node.letter == node.letter:
                current_node.count += 1
                return current_node
            elif current_node.letter < node.letter:
                current_node.right_child = self.add_helper(node, current_node.right_child, current_node)
            else:
                current_node.left_child = self.add_helper(node, current_node.left_child, current_node)

        return current_node
    def remove(self, node):
        delete_node = self.find(node)

        if delete_node is None:
            return None
        elif delete_node.left_child is None and delete_node.right_child is None:
            if delete_node.parent is None:
                self.root = None
                return
            if delete_node == delete_node.parent.left_child:
                delete_node.parent.left_child = None
            if delete_node == delete_node.parent.right_child:
                delete_node.parent.right_child = None

        # if self.size > 1:
        #     node_to_remove = self._get(key, self.root)
        #     if node_to_remove:
        #         self._delete(node_to_remove)
        #         self.size = self.size - 1
        #     else:
        #         raise KeyError("Error, key not in tree")
        # elif self.size == 1 and self.root.key == key:
        #     self.root = None
        #     self.size = self.size - 1
        # else:
        #     raise KeyError("Error, key not in tree")
    def height(self):
        """Height function"""
        return self.height_helper(self.root) + 1
    def height_helper(self, node):
        """Height function helper"""
        if node is None:
            return -1
        else:
            left_depth = self.height_helper(node.left_child)
            right_depth = self.height_helper(node.right_child)

            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
    def size(self):
        """Size function"""
        return self._size
    def find(self, node):
        """find function"""
        node = self.find_helper(self.root, node.letter)
        return node
    def find_helper(self, node, letter):
        """Find function helper"""
        if node is None:
            raise ValueError("Node not found")
        if node.letter == letter:
            return node
        if node.letter < letter:
            return self.find_helper(node.right_child, letter)
        return self.find_helper(node.left_child, letter)
    def get_root_val(self):
        """Get root value function"""
        return self.root
    def set_root_val(self, new_obj):
        """Set root value function"""
        self.root = new_obj
    def is_empty(self):
        """Is Empty function"""
        if self.root is None:
            return True
        else:
            return False
    def inorder(self):
        """inorder function"""
        lyst = []
        self.in_order_helper(self.root, lyst)
        return lyst
    def in_order_helper(self, node, lyst):
        """In Order function helper"""
        if node:
            self.in_order_helper(node.left_child, lyst)
            lyst.append(node)
            self.in_order_helper(node.right_child, lyst)
    def preorder(self):
        """preorder function"""
        lyst = []
        self.pre_order_helper(self.root, lyst)
        return lyst
    def pre_order_helper(self, node, lyst):
        """Preorder function helper"""
        if node:
            lyst.append(node)
            self.pre_order_helper(node.left_child, lyst)
            self.pre_order_helper(node.right_child, lyst)
    def postorder(self):
        """postorder function"""
        lyst = []
        self.post_order_helper(self.root, lyst)
        return lyst
    def post_order_helper(self, node, lyst):
        """Preorder function helper"""
        if node:
            self.post_order_helper(node.left_child, lyst)
            self.post_order_helper(node.right_child, lyst)
            lyst.append(node)
