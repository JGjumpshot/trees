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
        self.letter = letter
        self.count = count
        self.parent = None
        self.right_child = None
        self.left_child = None
        
    def is_leaf(self):
        return not (self.right_child or self.left_child)
    def has_a_child(self):
        return self.right_child or self.left_child
    def has_children(self):
        return self.right_child and self.left_child
    def find_successor(self):
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
        current = self
        while current.left_child:
            current = current.left_child
        return current
    def splice_out(self):
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
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self
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
        # print(Pair(ord(i)))
    return my_tree


def main():
    # make_tree()
    # my_file = open("around-the-world-in-80-days-3.txt")
    # x = my_file.read()
    # for i in punctuation:
    #     x = x.replace(i, "")
    # for i in whitespace:
    #     x = x.replace(i, "")
    # for i in x:
    #     print(Pair(ord(i)))
    # myTree.add_node(myNode3)
    # myTree.add_node(myNode4)
    # print(make_tree().size)
    # my_node = Pair('b', 20)
    # my_node.left_child = Pair('a', 10)
    # my_node.left_child.left_child = Pair('z', 12)
    # my_node.right_child = Pair('z', 20)
    # my_node.right_child.right_child = Pair('e', 20)
    # my_node.right_child.right_child.right_child = Pair('f', 12)
    # my_tree = BinarySearchTree(my_node)
    # my_tree.add(Pair("a", 20))
    test = make_tree()
    # print(test.inorder())
    print(test.remove(Pair("r")))
    print(test.inorder())
    # print(my_tree.find(my_node, 'z'))
    # print(my_tree.height(my_node))
    # print(my_tree.size(my_node))
    
    # print(my_tree.in_order(my_node)) ****
        # print(make_tree())
    # print(x)
    # x = x.replace(" ", "")

if __name__ == "__main__":
    main()
