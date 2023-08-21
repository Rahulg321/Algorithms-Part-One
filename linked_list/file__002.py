# the entire programs for a doubly linkedlist


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        new_node = Node(value)
        temp = self.head

        # if head exits
        if temp:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node

    def insert_specific(self, value, index):
        new_node = Node(value)
        count = 0
        temp = self.head

        if temp is None:
            print(" insert at the first position")
            self.head = new_node
            return

        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        elif index < 0:
            print("please enter a valid index")
            return

        while count < index:
            prev_node = temp
            temp = temp.next
            if temp is None:
                print("index was out of range of the length of the list")
                print("if you want to insert at the end insert a different function")
                return
            count += 1

        # print("prevNode => ", prev_node.value)
        # print("curNode => ", temp.value)

        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = temp
        temp.prev = new_node

    def insert_end(self, value):
        new_node = Node(value)
        temp = self.head
        if temp:
            while temp.next is not None:
                temp = temp.next

            print("value of last node is ", temp.value)
            temp.next = new_node
            new_node.prev = temp

    def delete_node(self, value):
        # prev_node = None

        if value == self.head.value:
            self.head = self.head.next
            return

        temp = self.head

        while temp:
            if temp.value == value:
                # print("we found the about to be deleted node")
                break

            prev_node = temp
            temp = temp.next

        if temp:
            print("the deleted node was found")
            prev_node.next = temp.next
            temp.next.prev = prev_node
            return 
        else:
            print("the node does not exist in this list")
            return

    # def delete_first(self):
    #     self.head = self.head.next

    # def delete_last(self):
    #     temp = self.head

    #     if temp is None:
    #         print("the list does not exist")
    #         return

    #     if self.head.next is None:
    #         self.head = None
    #         return

    #     while temp.next is not None:
    #         prev_node = temp
    #         temp = temp.next

    #     # since it is the last node
    #     prev_node.next = None

    def traverse_forward(self):
        print("forward traversal")
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next

    def traverse_backward(self):
        print("backward traversal")
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        while temp.prev is not None:
            print(temp.value, end="<-")
            temp = temp.prev


ll = LinkedList()

ll.insert_begin(3)
ll.insert_begin(2)
ll.insert_begin(1)

ll.insert_specific(43, 1)


ll.traverse_forward()
# ll.traverse_backward()
