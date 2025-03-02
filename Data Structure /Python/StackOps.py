class Stack:
    def __init__(self, maxSize):
        self.stack = [None] * maxSize  # Initialize a fixed-size list
        self.maxSize = maxSize
        self.top = -1  # Initialize top as -1 to indicate an empty stack

    def is_full(self):
        if self.top == self.maxSize - 1 : 
            print("Stack Overflow")
        else : 
            print("Stack is not Full")

    def is_empty(self):
        if self.top == -1 :
            print("Stack Undeflow")
        else : 
            print("Stack is not Empty")
    
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

    def peek(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print(f"Top element is : {self.stack[self.top]}") 

    def display(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Stack elements are :")
            for i in range(self.top, -1, -1):
                print(f"Pointer = {i} : Item = {self.stack[i]}" )

maxSize = int(input("Enter the maximum size of the stack: "))
stack = Stack(maxSize)

while True:
    print("\n--- Stack Operations Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Full")
    print("5. Is Empty")
    print("6. Display")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to push: ")
        stack.push(item)
    elif choice == 2: stack.pop()
    elif choice == 3: stack.peek()
    elif choice == 4: stack.is_full()
    elif choice == 5: stack.is_empty()
    elif choice == 6: stack.display()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
