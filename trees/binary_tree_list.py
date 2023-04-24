#in this file we will implement a binary tree from Python List
class BinaryTree:
    def __init__(self, size = 5):
        self.custom_list = [None] * size
        self.last_used_index = 0
        self.max_size = size

BT = BinaryTree(8)