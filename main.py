'''
Project:
Author: 
Course: 
Date: 

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import *


class Pair:
    ''' Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators. 
    '''

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count
        self.right_child = None
        self.left_child = None
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
    """A helper function to build the tree.The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree"""
    my_tree = BinarySearchTree()
    return my_tree


def main():
    ''' Program kicks off here.

    '''
    # my_file = open("around-the-world-in-80-days-3.txt")
    
    # x = my_file.read()

    # for i in punctuation:
    #     x = x.replace(i, "")
    # for i in whitespace:
    #     x = x.replace(i, "")

    # for i in x:
    #     print(Node(ord(i)))
    
    # myTree.add_node(myNode3)
    # myTree.add_node(myNode4)
    # print(make_tree().size)
    my_node = Pair('b', 20)
    my_node.left_child = Pair('a', 10)
    my_node.left_child.left_child = Pair('z', 12)
    my_node.right_child = Pair('z', 20)
    my_node.right_child.right_child = Pair('e', 20)
    my_node.right_child.right_child.right_child = Pair('f', 12)
    my_tree = BinarySearchTree(my_node)
    # print(my_tree.find(my_node, 'a'))
    print(my_tree.height(my_node))
    print(my_tree.size(my_node))
        # print(make_tree())
    # print(x)
    # x = x.replace(" ", "")

if __name__ == "__main__":
    main()
