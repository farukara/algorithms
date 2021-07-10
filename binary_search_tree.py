#!python3
#implements binary search tree

import random

class BST():
    '''
    binary search tree implementaion
    '''

    def __init__(self):
        self.root = None

    def insert(self, value):
        
        item = bstnode(value)
        if self.root == None:
            self.root = item
            return
        node = self.root
        while True:
            if value == node.value:
                item.parent = node.parent
                item.rightchild = node
                node.parent = item
                break
            elif value < node.value:
                if node.leftchild:
                    if value > node.leftchild.value:
                        item.parent = node
                        item.leftchild = node.leftchild
                        node.leftchild.parent = item
                        node.leftchild = item
                        break
                    node = node.leftchild
                else:
                    node.leftchild = item
                    item.parent = node
                    break
            else:
                if node.rightchild:
                    if value < node.rightchild.value:
                        item.parent = node
                        item.rightchild = node.rightchild
                        node.rightchild.parent = item
                        node.rightchild = item
                        break
                    node = node.rightchild
                else:
                    node.rightchild = item
                    item.parent = node
                    break

    def find(self, value):
        node = self.root
        while node is not None:
            if node.value == value:
                return node
            elif node.value > value:
                node = node.leftchild
            else:
                node = node.rightchild
        return None

    def remove(self, value):
        pass
        
    def __str__(self):
        node = self.root
        def printnode(node):
            print(node.value)
            if node.leftchild:
                print(node.leftchild.value)
                printnode(node.leftchild)
            if node.rightchild:
                print(node.rightchild.value)
                printnode(node.rightchild)
        
        printnode(node)
        #while node is not None:
        #    if node.leftchild:
        #        print(node.leftchild.value, end=" ")
        #    if node.rightchild:
        #        print(node.rightchild.value)
        #    node = node.leftchild
        return "end"


class bstnode():
    '''
    creates a node with parent and childrens
    '''

    def __init__(self, value, parent=None, leftchild=None, rightchild=None):
        self.value = value
        self.parent = parent
        self.leftchild = leftchild
        self.rightchild = rightchild
    
    def disconnect(self):
        self.parent = None
        self.leftchild = None
        self.rightchild = None
        

if __name__ == "__main__":
    agac = BST()
    for i in range(10):
        agac.insert(i) #random.randrange(10))
    print(agac)
