class CircularQueue:
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = -1
        self.rear = -1

    def is_full(self):
        if (self.rear + 1) % self.maxsize == self.front: 
            print("Queue Overflow")
        else : 
            print("Queue is not Full")

    def is_empty(self):
        if self.front == -1 : 
            print("Queue Undeflow")
        else : 
            print("Queue is not Empty")

    def enqueue(self):
        if (self.rear + 1) % self.maxsize == self.front: 
            print("Queue Overflow")
        else:
            item = input("Enter the item to enqueue: ")
            if self.front == -1:  # First insertion
                self.front = 0
            self.rear = (self.rear + 1) % self.maxsize
            self.queue[self.rear] = item
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.front == -1 : 
            print("Queue Undeflow")
        else:
            print(f"Dequeued: {self.queue[self.front]}")
            if self.front == self.rear:  # Queue becomes empty
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.maxsize

    def peek(self):
        if self.front == -1 : 
            print("Queue Undeflow")
        else:
            print(f"Front element: {self.queue[self.front]}")

    def display(self):
        if self.front == -1 : 
            print("Queue Undeflow")
        else:
            print("Queue contents:", end=" ")
            if self.rear >= self.front:
                # No wrapping around
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")
            else:
                # Wrapping around the circular queue
                for i in range(self.front, self.maxsize):
                    print(self.queue[i], end=" ")
                for i in range(0, self.rear + 1):
                    print(self.queue[i], end=" ")
            print()

# Example usage
queue_size = int(input("Enter the maximum size of the circular queue: "))
cq = CircularQueue(queue_size)

while True:
    print("\n--- Circular Queue Operations ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Is Full")
    print("5. IS Empty")
    print("6. Display Queue")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:     cq.enqueue()
    elif choice == 2:   cq.dequeue()
    elif choice == 3:   cq.peek()
    elif choice == 4:   cq.is_full()
    elif choice == 5:   cq.is_empty()
    elif choice == 6:   cq.display()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
