# deque => combined stack and queue
# allows insertion and deletion from both ends


class Deque:
    def __init__(self) -> None:
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, element):
        self.item.insert(0, element)

    def add_rear(self, element):
        self.item.append(element)
        
    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is empty")

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Deque is empty")

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is empty")

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is empty")

    def __str__(self):
        return str(self.items)