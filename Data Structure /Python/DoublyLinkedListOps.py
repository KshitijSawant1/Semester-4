# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"Inserted {data} at the end.")

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        print(f"Deleted {self.head.data} from the beginning.")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:  # Only one node
            print(f"Deleted {self.head.data} from the end.")
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        print(f"Deleted {current.data} from the end.")
        current.prev.next = None

    def display_forward(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        print("Doubly Linked List (Forward):", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current.next:
            current = current.next
        print("Doubly Linked List (Backward):", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Menu-driven program
if __name__ == "__main__":
    dll = DoublyLinkedList()
    while True:
        print("\n--- Doubly Linked List Operations ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete from Beginning")
        print("4. Delete from End")
        print("5. Display Forward")
        print("6. Display Backward")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            dll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            dll.insert_at_end(data)
        elif choice == 3:
            dll.delete_from_beginning()
        elif choice == 4:
            dll.delete_from_end()
        elif choice == 5:
            dll.display_forward()
        elif choice == 6:
            dll.display_backward()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
