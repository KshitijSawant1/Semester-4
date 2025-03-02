class Queue:
    def __init__(self):
        # Initialize two stacks for queue simulation
        self.s1 = [None] * 5
        self.s2 = [None] * 5
        self.s1_top = -1  # Top pointer for stack s1
        self.s2_top = -1  # Top pointer for stack s2
        self.max_size = 5

    def push_stack(self, stack, item, top):
        if top == self.max_size - 1:
            print("Stack Overflow")
        else:
            top += 1
            stack[top] = item
        return top

    def pop_stack(self, stack, top):
        if top == -1:
            print("Stack Underflow")
            return None, top
        else:
            item = stack[top]
            top -= 1
            return item, top

    def enQueue(self, x):
        # Move all elements from s1 to s2
        while self.s1_top != -1:
            item, self.s1_top = self.pop_stack(self.s1, self.s1_top)
            self.s2_top = self.push_stack(self.s2, item, self.s2_top)

        # Push the new element onto s1
        self.s1_top = self.push_stack(self.s1, x, self.s1_top)

        # Move all elements back to s1 from s2
        while self.s2_top != -1:
            item, self.s2_top = self.pop_stack(self.s2, self.s2_top)
            self.s1_top = self.push_stack(self.s1, item, self.s1_top)

    def deQueue(self):
        if self.s1_top == -1:
            print("Queue is empty.")
            return None
        # Pop the front element
        item, self.s1_top = self.pop_stack(self.s1, self.s1_top)
        return item

# Driver code
q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print(q.deQueue())  # Output: 1
print(q.deQueue())  # Output: 2
print(q.deQueue())  # Output: 32
print(q.deQueue())  # Output: Queue is empty. None
