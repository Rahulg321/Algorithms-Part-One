#implementing python binary tree using list as a practice

class BinaryTree:
    def __init__(self, size):
        self.last_used_index = 0
        self.max_size = size
        self.custom_list = [None] * size

    def insert_new_node(self, data):
        if self.is_full():
            return "the list is full"
        else:
            self.custom_list[self.last_used_index + 1] = data
            self.last_used_index += 1

    def search_node(self, value):
        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == value:
                return f"{value} found at index:{i}"

    def is_full(self):
        if self.last_used_index + 1 == self.max_size:
            return True
        return False

    def is_empty(self):
        if self.last_used_index == 0:
            return True
        return False

    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        else:
            self.in_order_traversal(2 * index)
            print(self.custom_list[index])
            self.in_order_traversal((2 * index) + 1)

    def level_order_traversal(self):
        for i in range(1, self.last_used_index + 1):
            print(self.custom_list[i])

        return

NewBT = BinaryTree(10)

NewBT.insert_new_node("Drinks")
NewBT.insert_new_node("Hot")
NewBT.insert_new_node("Cold")
NewBT.insert_new_node("Coffee")
NewBT.insert_new_node("Tea")

NewBT.in_order_traversal(1)
print("***********************")
NewBT.level_order_traversal()