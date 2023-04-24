import trees.queueLinkedList as q

class TreeNode():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


RahulBT = TreeNode("Rahul")
Dreams = TreeNode("Dreams")
SignificantOthers = TreeNode("Significant others")

RahulBT.left = Dreams
RahulBT.right = SignificantOthers

#for my dreams
GoodCompany = TreeNode("GoodCompany")
Money = TreeNode("Money")

#assigned values  to my dreams
Dreams.left = GoodCompany
Dreams.right = Money

#for  my significant others
GK = TreeNode("GK")
EGS = TreeNode("EGS")

SignificantOthers.left = GK
SignificantOthers.right = EGS


Friends = TreeNode("Friends")
Environment = TreeNode("Environment")

GoodCompany.left = Friends
GoodCompany.right = Environment


Dollar = TreeNode("Dollar")

Money.right = Dollar

PCTE = TreeNode("PCTE")

GK.left = PCTE


def preOrderTraversal(rootNode):
    """
        root -> left -> right
    """
    if rootNode is None:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)


def inOrderTraversal(rootNode):
    """
        left -> root -> right
    """
    if rootNode is None:
        return
    else:
        inOrderTraversal(rootNode.left)
        print(rootNode.data)
        inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    """
        left -> right -> root
    """
    if rootNode is None:
        return
    else:
        postOrderTraversal(rootNode.left)
        postOrderTraversal(rootNode.right)
        print(rootNode.data)


# print("Pre Order Traversal")
# preOrderTraversal(RahulBT)
#
# print()
#
# print("InOrder Traversal")
# inOrderTraversal(RahulBT)
#
# print()
#
# print("postOrderTraversal")
# postOrderTraversal(RahulBT)


def levelOrderTraversal(rootNode):
    """
    traversing a tree level by level
    """
    if rootNode is None:
        return
    else:
        custom_queue = q.Queue()
        custom_queue.enqueue(rootNode)

        while custom_queue.is_empty() is False:
            element = custom_queue.dequeue()
            print(element.value.data)

            if element.value.left is not None:
                custom_queue.enqueue(element.value.left)

            if element.value.right is not None:
                custom_queue.enqueue(element.value.right)


levelOrderTraversal(rootNode=RahulBT)