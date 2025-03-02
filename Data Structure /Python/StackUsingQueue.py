class Queue:
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.front = -1
        self.rear = -1
        self.maxsize = maxsize

    def enqueue(self, item):
        if self.rear == self.maxsize - 1:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item

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
            return item

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def front_element(self):
        if not self.is_empty():
            return self.queue[self.front]
        return None


class StackUsingQueues:
    def __init__(self, maxsize):
        self.q1 = Queue(maxsize)
        self.q2 = Queue(maxsize)
        self.maxsize = maxsize

    def push(self, item):
        # Push item into empty q2
        self.q2.enqueue(item)

        # Move all elements from q1 to q2
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1.is_empty():
            return self.q1.dequeue()
        else:
            print("Stack Underflow")
            return None

    def top(self):
        return self.q1.front_element()


# Example usage
maxsize = 5
stack = StackUsingQueues(maxsize)
stack.push(10)
stack.push(20)

stack.push(30)

print("Top element:", stack.top())  # Output should be 30
print("Popped element:", stack.pop())  # Removes 30
print("Top element after pop:", stack.top())  # Output should be 20