class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

queue = Queue()
queue.is_empty()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

#popped_item = queue.dequeue()
#print("Popped item: ", popped_item)

top_item = queue.peek()
print("Top item of the stack: ", top_item)

size = queue.size()
print("Size of stack: ", size)