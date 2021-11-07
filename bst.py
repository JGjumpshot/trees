"""Binary search tree"""
# from main import Pair


class BinarySearchTree:
    """init function"""

    def __init__(self, root_obj=None):
        self.root = root_obj
        self._size = 0
        # self.left_child = None
        # self.right_child = None

    def add(self, node):
        """add function"""
        self.root = self.add_helper(node, self.root)

    def add_helper(self, node, current_node, parent=None):
        """Add function helper"""
        if current_node is None:
            self._size += 1
            node.parent = parent
            return node
        else:
            if current_node.letter == node.letter:
                current_node.count += 1
                return current_node
            elif current_node.letter < node.letter:
                current_node.right_child = self.add_helper(
                    node, current_node.right_child, current_node)
            else:
                current_node.left_child = self.add_helper(
                    node, current_node.left_child, current_node)

        return current_node

    def remove(self, key):
        """remove a node"""
        if self._size > 1:
            node_to_remove = self.find(key)
            if node_to_remove:
                self._remove(node_to_remove)
                self._size = self._size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")

    def _remove(self, current_node):
        if current_node.is_leaf():  # removing a leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_children():  # removing a node with two children
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.letter = successor.letter
        else:  # removing a node with one child
            if current_node.left_child:
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )

    def __delitem__(self, key):
        self.remove(key)

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

    def rebalance(self):
        """rebalance function"""
        in_order_list = self.inorder()
        pointer = self.root
        if len(in_order_list) <= 1:
            return
        # elif pointer
        middle = (len(in_order_list) // 2)
        right_side = in_order_list[middle:]
        left_side = in_order_list[:middle]

        print(len(left_side))
        print(len(right_side))
        # if len(in_order_list) == 0:
        #     return
        # elif in_order_list[middle]
        # print(middle)
