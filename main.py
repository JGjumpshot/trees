# from pathlib import Path
"""Module docstring"""
from string import whitespace, punctuation
from bst import BinarySearchTree


class Pair:
    ''' Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators.
    '''

    def __init__(self, letter, count=1):
        """Init function"""
        self.letter = letter
        self.count = count
        self.parent = None
        self.right_child = None
        self.left_child = None

    def is_leaf(self):
        """Is leaf function"""
        return not (self.right_child or self.left_child)

    def has_a_child(self):
        """has a child function"""
        return self.right_child or self.left_child

    def has_children(self):
        """has children function"""
        return self.right_child and self.left_child

    def find_successor(self):
        """find successor function"""
        successor = None
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        """find minimum left child"""
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self):
        """splice node"""
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_a_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def is_left_child(self):
        """Is left child function"""
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        """Is right child function"""
        return self.parent and self.parent.right_child is self

    def is_balanced(self):
        """Is balanced function"""
        left_height = self.left_child.height() if self.left_child else 0
        right_height = self.right_child.height() if self.right_child else 0
        return abs(left_height - right_height < 2)

    def height(self):
        """Height function"""
        return self.height_helper(self.parent) + 1

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

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    """A helper function to build the tree.The test code depends on this
    function being available from main.
    :param: None
    :returns: A binary search tree"""
    my_tree = BinarySearchTree()
    my_file = open("around-the-world-in-80-days-3.txt", encoding="utf-8")
    read_lines = my_file.read()
    for i in punctuation:
        read_lines = read_lines.replace(i, "")
    for i in whitespace:
        read_lines = read_lines.replace(i, "")
    for i in read_lines:
        node = Pair(i)
        my_tree.add(node)
    return my_tree


def main():
    """Main function"""
    test = make_tree()
    print(test.height())


if __name__ == "__main__":
    main()
