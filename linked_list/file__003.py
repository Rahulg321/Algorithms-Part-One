# Cracking the Code interview
# remove duplicates from an unsorted linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        new_node = Node(value)
        temp = self.head

        if temp:
            new_node.next = temp
            self.head = new_node
        else:
            self.head = new_node

    def insert_specific(self, value, index):
        new_node = Node(value)
        count = 1
        temp = self.head

        if temp is None:
            print("the list is empty")
            print("you can insert at the first position")
            self.head = new_node
            return

        if index == 0:
            new_node.next = temp
            self.head = new_node
            return

        elif index < 0:
            print("please enter a valid index")
            return

        while count < index:
            temp = temp.next
            count += 1

        new_node.next = temp.next
        temp.next = new_node

    def insert_end(self, value):
        new_node = Node(value)
        temp = self.head
        if temp is None:
            # print("the list is empty")
            self.head = new_node
        else:
            while temp.next != None:
                temp = temp.next

            temp.next = new_node

    def delete_node(self, value):
        # prev_node = None

        if value == self.head.value:
            self.head = self.head.next
            return

        temp = self.head

        while temp:
            if temp.value == value:
                print("we found the about to be deleted node")
                break

            prev_node = temp
            temp = temp.next

        if temp:
            print("the deleted node was found")
            prev_node.next = temp.next
        else:
            print("the node does not exist in this list")
            return

    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        temp = self.head

        if temp is None:
            print("the list does not exist")
            return

        if self.head.next is None:
            self.head = None
            return

        while temp.next is not None:
            prev_node = temp
            temp = temp.next

        # since it is the last node
        prev_node.next = None

    def traverse_list(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next


ll = LinkedList()

ll.insert_end(11)
ll.insert_end(25)
ll.insert_end(37)
ll.insert_end(43)
ll.insert_end(50)
ll.insert_end(11)
ll.insert_end(89)
ll.insert_end(572)
ll.insert_end(11)

ll.traverse_list()



def remove_duplicates(linked_list):
    temp = self.head
