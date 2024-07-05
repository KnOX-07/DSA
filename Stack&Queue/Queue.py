'''class Queue:
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
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

#popped_item = queue.dequeue()
#print("Popped item: ", popped_item)

top_item = queue.peek()
print("Top item of the stack: ", top_item)

size = queue.size()
print("Size of stack: ", size)'''

class Queue:
    def __init__(self, max_size):
        self.l = [0] * max_size  # Initialize the list with zeros of size max_size
        self.max = max_size  # Define the maximum size of the queue
        self.front = -1  # Initialize front with -1 indicating the queue is empty
        self.rear = -1  # Initialize rear with -1 indicating the queue is empty

    def insertion(self, element):
        if (self.rear + 1) % self.max == self.front:
            print('Queue Overflow. Cannot insert to the queue.')
            return
        if self.front == -1:  # If the queue is initially empty
            self.front = 0
        self.rear = (self.rear + 1) % self.max  # Move rear to the next position
        self.l[self.rear] = element  # Insert the new element
        print(f'Inserted {element} to queue. Queue is now: {self.l}')

    def deletion(self):
        if self.front == -1:
            print('Queue Underflow. Cannot delete from the queue.')
            return None
        element = self.l[self.front]  # Get the front element
        if self.front == self.rear:  # If the queue is now empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max  # Move front to the next position
        print(f'Deleted {element} from queue. Queue is now: {self.l}')
        return element

    def traverse(self):
        if self.front == -1:
            print('Queue is empty.')
            return
        print('Queue elements are:')
        i = self.front
        while True:
            print(self.l[i], end=' ')
            if i == self.rear:
                break
            i = (i + 1) % self.max
        print()  # For a new line

queue = Queue(5)  # Create a queue with maximum size 5

queue.insertion(10)
queue.insertion(20)
queue.insertion(30)
queue.traverse()

queue.deletion()
queue.traverse()