# this is used as as a helper class for level order traversal  in tree
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            temp = temp.next


class Queue:
    def __init__(self):
        self.Queue = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.Queue]
        return " <-> ".join(values)

    def is_empty(self):
        if self.Queue.head is None:
            return True

    def enqueue(self, data):
        newNode = Node(data)

        # the list is empty
        if self.is_empty():
            self.Queue.head = newNode
            self.Queue.tail = newNode
        else:
            self.Queue.tail.next = newNode
            self.Queue.tail = newNode

    def dequeue(self):
        # if the list is empty
        if self.is_empty():
            return f'The queue is empty'
        else:
            # if there is only  one element
            if self.Queue.head == self.Queue.tail:
                element = self.Queue.head
                self.Queue.head = None
                self.Queue.tail = None
                return element
            else:
                element = self.Queue.head
                self.Queue.head = self.Queue.head.next
                return element


# q1 = Queue()

# q1.enqueue("1")
# q1.enqueue("2")
# q1.enqueue("3")
# q1.enqueue("4")
# q1.enqueue("5")

# q1.dequeue()

# print(q1)
