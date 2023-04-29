# in this file we will implement a binary tree from Python List

import queueLinkedList as queue

class BinaryTreeList:

    def __init__(self, size):
        self.custom_list = [None] * size
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, data):
        """
            space-complex: 0(n)
            time-complex: 0(1)
        """
        if self.last_used_index + 1 == self.max_size:
            return "the list is full"
        else:
            self.custom_list[self.last_used_index + 1] = data
            self.last_used_index += 1
            return "the value has been inserted"

#search for a node using python list

    def search_node(self, value):
        """
        space-complex: 0(1)
        time-complex: 0(n)
        """
        for element in self.custom_list:
            if element == value:
                return "node was found"
        return "element not found"

    def pre_order_traversal(self, index):
        """
        root -> left -> right
        """
        # if currIndex exceeds the last used index in list
        if index > self.last_used_index:
            return
        else:
            print(self.custom_list[index])
            self.pre_order_traversal(2 * index)
            self.pre_order_traversal((2*index) + 1)

    def post_order_traversal(self, index):
        """
        left -> right -> root
        """
        if index > self.last_used_index:
            return
        else:
            self.post_order_traversal(2 * index)
            self.post_order_traversal((2*index) + 1)
            print(self.custom_list[index])

    def in_order_traversal(self, index):
        """
        left -> root -> right
        """
        if index > self.last_used_index:
            return
        else:
            self.in_order_traversal(2 * index)
            print(self.custom_list[index])
            self.in_order_traversal((2*index) + 1)

    def level_order_traversal(self):
        for i in range(1, self.last_used_index + 1):
            print(self.custom_list[i])

        return

    def delete_tree(self):
        self.custom_list = [None] * self.max_size
        return

    def get_deepest_node(self):
        return self.custom_list[self.last_used_index]


    def delete_node(self, value):
        last_node = self.get_deepest_node()
        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == value:
                self.custom_list[self.last_used_index] = None
                self.custom_list[i] = last_node
                self.last_used_index -= 1
                return "element successfully deleted"

        return "node was not present in the list"




NewBT = BinaryTreeList(10)

NewBT.insert_node("Drinks")
NewBT.insert_node("Hot")
NewBT.insert_node("Cold")
NewBT.insert_node("Tea")
NewBT.insert_node("Coffee")
NewBT.insert_node("Fanta")
NewBT.insert_node("Cola")

# print("pre order traversal [root -> left -> right]")
# NewBT.pre_order_traversal(1)

# print("post_order_traversal [left -> right -> root]")
# NewBT.post_order_traversal(1)

# print("in_order_traversal [left -> root -> right]")
# NewBT.in_order_traversal(1)



print("level_order_traversal")
NewBT.level_order_traversal()

print("calling the delete method")
NewBT.delete_node("Drinks")


print("level_order_traversal")
NewBT.level_order_traversal()
