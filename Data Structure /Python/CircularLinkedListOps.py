class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.head = new_node
            current.next = self.head
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        print(f"Inserted {data} at the end.")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return
        current = self.head
        for _ in range(position - 2):
            if current.next == self.head:
                print("Position out of range.")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at position {position}.")

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            print(f"Deleted {self.head.data} from the beginning.")
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            print(f"Deleted {self.head.data} from the beginning.")
            self.head = self.head.next
            current.next = self.head

    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            print(f"Deleted {self.head.data} from the end.")
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            print(f"Deleted {current.next.data} from the end.")
            current.next = self.head

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty.")
            return
        if position == 1:
            self.delete_from_beginning()
            return
        current = self.head
        for _ in range(position - 2):
            if current.next == self.head:
                print("Position out of range.")
                return
            current = current.next
        if current.next == self.head:
            print("Position out of range.")
            return
        print(f"Deleted {current.next.data} from position {position}.")
        current.next = current.next.next

    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Menu-driven program

cll = CircularLinkedList()
while True:
        print("\n--- Circular Linked List Operations ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete from Beginning")
        print("5. Delete from End")
        print("6. Delete at Position")
        print("7. Display")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            cll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            cll.insert_at_end(data)
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position: "))
            cll.insert_at_position(data, position)
        elif choice == 4:
            cll.delete_from_beginning()
        elif choice == 5:
            cll.delete_from_end()
        elif choice == 6:
            position = int(input("Enter position to delete: "))
            cll.delete_at_position(position)
        elif choice == 7:
            cll.display()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
