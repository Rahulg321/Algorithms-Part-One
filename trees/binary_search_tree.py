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
        if root_node.data <= node_value:
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


newBST = TreeNode()
insert_new_node(newBST, 70)
insert_new_node(newBST, 50)
insert_new_node(newBST, 90)

print("inserting a new element")
print(newBST.data)
