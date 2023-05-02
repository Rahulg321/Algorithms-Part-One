# binary tree can be created by using array and linked lists

# creating binary tree using Linked Lists

# *******OPERATIONS*************
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

        # while custom queue is not empty
        while not (customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data, end=" -▶ ")

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

        while not (customQueue.is_empty()):
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

        while not (customQueue.is_empty()):
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
    the last node after level order Traversal is the deepest Node
    """

    element = None

    if rootNode is None:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        # while it returns False
        while not (customQueue.is_empty()):
            root = customQueue.dequeue()

            element = root.value
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

        return element


def delete_deepest_node(rootNode):
    """
    this function deletes the deepest node from a binary Tree
    """
    if not rootNode:  # if the rootNode is None
        return
    else:
        deepest_node = getDeepestNode(rootNode)
        custom_queue = queue.Queue()
        custom_queue.enqueue(rootNode)
        while custom_queue.is_empty() is False:
            root = custom_queue.dequeue()

            if root.value is deepest_node:
                print("The deepest Node was deleted")
                root.value.data = None

            if root.value.leftChild:
                if root.value.leftChild is deepest_node:
                    print("The deepest Node was deleted")
                    root.value.leftChild = None
                else:
                    custom_queue.enqueue(root.value.leftChild)

            if root.value.rightChild:
                if root.value.rightChild is deepest_node:
                    print("The deepest Node was deleted")
                    root.value.rightChild = None
                else:
                    custom_queue.enqueue(root.value.rightChild)


def delete_node(rootNode, d_node):
    if rootNode is None:
        return
    else:
        deepest_node = getDeepestNode(rootNode)

        custom_queue = queue.Queue()
        custom_queue.enqueue(rootNode)

        while custom_queue.is_empty() is False:
            root = custom_queue.dequeue()

            if root.value is d_node:
                root.value.data = deepest_node.data
                delete_deepest_node(rootNode)
                break

            if root.value.leftChild is not None:
                custom_queue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                custom_queue.enqueue(root.value.rightChild)


levelOrderTraversal(BT)
print()

print("Deleting a specific node from the Tree")
delete_node(rootNode=BT, d_node=milk)
levelOrderTraversal(BT)
