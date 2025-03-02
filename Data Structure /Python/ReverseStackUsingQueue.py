class Stack:
    def __init__(self, maxSize):
        self.stack = [None] * maxSize
        self.top = -1
        self.maxSize = maxSize

    def push(self, item):
        if self.top == self.maxSize - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"Pushed {item} onto the stack.")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            item = self.stack[self.top]
            self.top -= 1
            print(f"Popped {item} from the stack.")
            return item
    
    def is_empty(self):
        return self.top == -1

    def display(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Stack contents (top to bottom):", end=" ")
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()


class Queue:
    def __init__(self, maxSize):
        self.queue = [None] * maxSize
        self.front = -1
        self.rear = -1
        self.maxSize = maxSize

    def enqueue(self, item):
        if self.rear == self.maxSize - 1:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return None
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            print(f"Dequeued {item} from the queue.")
            return item

    def is_empty(self):
        return self.front == -1 or self.front > self.rear


def reverse_stack(stack):
    queue = Queue(stack.maxSize)
    
    print("Transfer all elements from stack to queue" )
    while not stack.is_empty():
        item = stack.pop()
        if item is not None:
            queue.enqueue(item)
        print()

    print("Transfer elements back to stack from queue (in reverse order)")
    while not queue.is_empty():
        print()
        stack.push(queue.dequeue())


# Example Usage
stack = Stack(5)
stack.push(40)
stack.push(30)
stack.push(20)
stack.push(10)

print("\nOriginal Stack:")
stack.display()

# Reverse the stack
reverse_stack(stack)

print("\nReversed Stack:")
stack.display()
