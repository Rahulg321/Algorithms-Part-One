class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next


ll = LinkedList() 
one = Node(1)
two = Node(2)
third = Node(3)
fourth = Node(4)
ll.head = one
one.next = two
two.next = third

third.next = fourth

fourth.next = two

hash = {}


temp = ll.head

while temp:
    if temp not in hash:
        hash[temp] = 1
    else:
        print("already in hash loop point detected",temp.value)
        break

    temp = temp.next

print(hash)
