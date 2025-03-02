class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = [None] * maxsize 
        self.front = -1
        self.rear = -1

    def is_full(self):
        if self.rear == self.maxsize - 1 : 
            print("Queue Overflow")
        else : 
            print("Queue is not Full")

    def is_empty(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Undeflow")
        else : 
            print("Queue is not Empty")
            
    def enqueue(self):
        item = input("Enter the item to Enqueue : ")
        if self.rear == self.maxsize - 1 : 
            print("Queue Overflow")
        else: 
            if self.front == -1 : 
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(f"Value Inserted : {item}")
            
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Undeflow")
        else :
            print(f"Value Deleted : {self.queue[self.front]}")
            if self.front ==  self.rear : 
                self.front = self.rear = -1
            else: 
                self.front += 1
                
    def peek(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Undeflow")
        else: 
            print(f"Front element is : {self.queue[self.front]}")     

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Undeflow")
        else:
            print("Queue contents:", end=" ")
            for i in range(self.front,self.rear+1,1):
                print(f"Pointer = {i} : Item = {self.queue[i]}" )

maxsize = int(input("Enter the maximum size of the Queue : "))
queue = Queue(maxsize)

while True:
    print("\n--- Queue Operations Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Is Full")
    print("5. Is Empty")
    print("6. Display")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:     queue.enqueue()
    elif choice == 2:   queue.dequeue()
    elif choice == 3:   queue.peek()
    elif choice == 4:   queue.is_full()
    elif choice == 5:   queue.is_empty()
    elif choice == 6:   queue.display()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")