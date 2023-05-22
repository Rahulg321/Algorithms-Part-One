import queueLinkedList as queue


class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


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

        while not (custom_queue.is_empty()):
            element = custom_queue.dequeue()

            print(element.value.data, end=" -> ")

            if element.value.left_child is not None:
                custom_queue.enqueue(element.value.left_child)

            if element.value.right_child is not None:
                custom_queue.enqueue(element.value.right_child)


def search_node(root_node, node_value):
    if root_node is None:
        return False

    if root_node.data < node_value:
        search_node(root_node.right_child, node_value)

    elif root_node.data > node_value:
        search_node(root_node.left_child, node_value)

    else:
        print("Element found!")
        return True


def insert_node(root_node, node_value):
    if root_node is None:
        new_node = AVLNode(node_value)
        root_node = new_node
        return root_node

    else:
        if root_node.data < node_value:
            if root_node.right_child is None:
                new_node = AVLNode(node_value)
                root_node.right_child = new_node
            
            else:
                insert_node(root_node.right_child, node_value)
        
        elif root_node.data >= node_value:
            if root_node.left_child is None:
                new_node = AVLNode(node_value)
                root_node.left_child = new_node
            
            else:
                insert_node(root_node.left_child, node_value)

Tree = AVLNode(70)

insert_node(Tree, 50)
insert_node(Tree, 75)
insert_node(Tree, 45)
insert_node(Tree, 55)

level_order_traversal(root_node=Tree)


# print(search_node(Tree, 10))
