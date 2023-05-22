"""
similar to binary tree
+
left subtree has values less than the parent node
right subtree has values greater than the parent node
"""
import queueLinkedList as queue


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_new_node(root_node, node_value):
    # we check whether the list is empty
    if root_node.data is None:
        root_node.data = node_value

    else:
        if root_node.data < node_value:
            if root_node.right_child is None:
                new_node = TreeNode(node_value)
                root_node.right_child = new_node
            else:
                insert_new_node(root_node.right_child, node_value)
        else:
            if root_node.left_child is None:
                new_node = TreeNode(node_value)
                root_node.left_child = new_node
            else:
                insert_new_node(root_node.left_child, node_value)

        return "the node was inserted"


def pre_order_traversal(root_node):
    """
    root -> left -> right
    """
    if root_node is None:
        return
    else:
        print(root_node.data, end=" -> ")
        pre_order_traversal(root_node.left_child)
        pre_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    """
    left -> right -> root
    """
    if root_node is None:
        return
    else:
        post_order_traversal(root_node.left_child)
        post_order_traversal(root_node.right_child)
        print(root_node.data, end=" -> ")


def in_order_traversal(root_node):
    """
    left -> root -> right
    """
    if root_node is None:
        return
    else:
        in_order_traversal(root_node.left_child)
        print(root_node.data, end=" -> ")
        in_order_traversal(root_node.right_child)


def level_order_traversal(root_node):
    if root_node is None:
        return "rootNode is empty"
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)

        while not(custom_queue.is_empty()):
            element = custom_queue.dequeue()

            print(element.value.data, end=" -> ")

            if element.value.left_child is not None:
                custom_queue.enqueue(element.value.left_child)

            if element.value.right_child is not None:
                custom_queue.enqueue(element.value.right_child)


def search_node(root_node, node_value):
    if root_node.data == node_value:
        print("node was found")

    elif root_node.data > node_value:
        if root_node.left_child.data == node_value:
            print(f"Element {node_value} was found at {root_node.data} leftchild-> {root_node.left_child.data}")
        else:
            search_node(root_node.left_child, node_value)

    else:
        if root_node.right_child.data == node_value:
            print(f"Element {node_value} was found at {root_node.data} rightChild-> {root_node.right_child.data}")
        else:
            search_node(root_node.right_child, node_value)


def min_value_node(bstNode):
    """
    finding the node with the minimum value
    """
    current = bstNode

    while current.left_child is not None:
        current = current.left_child

    return current


def delete_node(root_node, node_value):
    if root_node is None:
        return root_node

    elif root_node.data > node_value:
        root_node.left_child = delete_node(root_node.left_child, node_value)

    elif root_node.data < node_value:
        root_node.right_child = delete_node(root_node.right_child, node_value)

    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp

        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp

        temp = min_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)

    return root_node


newBST = TreeNode()

insert_new_node(newBST, 70)
insert_new_node(newBST, 50)
insert_new_node(newBST, 90)
insert_new_node(newBST, 30)
insert_new_node(newBST, 60)
insert_new_node(newBST, 20)
insert_new_node(newBST, 40)
insert_new_node(newBST, 80)
insert_new_node(newBST, 100)

# pre_order_traversal(newBST)
# print()
# post_order_traversal(newBST)
# print()
# in_order_traversal(newBST)


level_order_traversal(root_node=newBST)
print()


print(min_value_node(newBST).data)

delete_node(newBST, 20)

level_order_traversal(root_node=newBST)
print()

# min_node = min_value_node(newBST.right_child)
# print(min_node.data)
