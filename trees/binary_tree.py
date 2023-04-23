# binary tree can be created by using array and linked lists

# creating binary tree using Linked Lists

#*******OPERATIONS*************
# creation of a tree
# insertion of  a node
# deletion of  a node
# search for a value
# traverse all nodes
# deletion of entire tree

import queueLinkedList as queue


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None


BT = TreeNode("Drinks")

hot = TreeNode("Hot")
cold = TreeNode("Cold")


coffee = TreeNode("Coffee")
tea = TreeNode("Tea")

fanta = TreeNode("Fanta")
milk = TreeNode("Milk")

BT.leftChild = hot
BT.rightChild = cold

hot.leftChild = coffee
hot.rightChild = tea

cold.leftChild = fanta
cold.rightChild = milk


def preOrderTraversal(rootNode):
    # root -> left -> right
    if rootNode is None:
        return
    print(rootNode.data, end=" -> ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    # left -> root -> right
    if rootNode is None:
        return

    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" -> ")
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    # left -> right ->  root
    if rootNode is None:
        return

    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" -> ")


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

# while it returns False
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data, end="-> ")

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchBT(rootNode, nodeValue):

    is_found = False

    if rootNode.data is None:
        return 'The binary Tree does not exist'

    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data, end="  -> ")
            if root.value.data == nodeValue:
                is_found = True
                print()

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

        print()
        if is_found:
            return f'element was found'
        else:
            return f'element does not exist in the tree'


def insertNewNode(rootNode, newNode):
    if rootNode is None:
        rootNode = newNode
        return 'element successfully inserted'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.is_empty()):
            root = customQueue.dequeue()

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                print()
                return 'element successfully inserted'

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                print()
                return 'element successfully inserted'


def getDeepestNode(rootNode):
    """
    this method returs the  deepest node from the tree by doing levelOrderTraversal
    """

    element = None

    if rootNode is None:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

# while it returns False
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()

            element = root.value
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

        return element

