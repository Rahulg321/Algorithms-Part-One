# my way
class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    # def __iter__(self):
    #     for x in self.queue:
    #         yield str(x)

    def __str__(self) -> str:
        values = [str(x) for x in self.queue]
        return " ".join(values)


q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

q1.dequeue()

print(q1)

len(q1)
