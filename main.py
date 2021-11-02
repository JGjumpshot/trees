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
    ''' A helper function to build the tree.

    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    pass


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
    myNode1 = Node(10)
    myNode2 = Node(2)
    myNode3 = Node(15)
    myNode4 = Node(5)

    myTree = BinarySearchTree(myNode1)
    myTree.add_node(myNode2)
    myTree.add_node(myNode3)
    myTree.add_node(myNode4)
    print(myTree)
        # print(make_tree())
    # print(x)
    # x = x.replace(" ", "")

if __name__ == "__main__":
    main()
