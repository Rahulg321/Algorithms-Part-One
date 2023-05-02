#practicing for binary search Tree

class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_new_node(root_node, value):
    """
    inserting a node to binary search Tree
    """
    if root_node.data is None:
        root_node.data = value
    else:
        if root_node.data <= value:
            if root_node.left_child is None:
                new_node = TreeNode(value)
                root_node.left_child = new_node
            else:
                insert_new_node(root_node.left_child, value)

        else:
            if root_node.right_child is None:
                new_node = TreeNode(value)
                root_node.right_child = new_node
            else:
                insert_new_node(root_node.left_child, value)




new_tree = TreeNode()

insert_new_node(new_tree, 70)
insert_new_node(new_tree, 50)
insert_new_node(new_tree, 90)

print(new_tree.data)