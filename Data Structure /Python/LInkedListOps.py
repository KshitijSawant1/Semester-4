class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # The pointer/reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list with no head node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position {position}.")
            return

        current = self.head
        previous = None
        count = 1

        while current and count < position:
            previous = current
            current = current.next
            count += 1

        if count == position:
            new_node.next = current
            if previous:
                previous.next = new_node
            print(f"Inserted {data} at position {position}.")
        else:
            print("Position out of range.")

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        print(f"Deleted {self.head.data} from the beginning.")
        self.head = self.head.next

    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            print(f"Deleted {self.head.data} from the end.")
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        print(f"Deleted {current.next.data} from the end.")
        current.next = None

    def delete_node(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print(f"Node with value {key} not found.")
            return
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Deleted node with value {key}.")

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty.")
            return
        if position == 1:
            print(f"Deleted {self.head.data} from position {position}.")
            self.head = self.head.next
            return
        current = self.head
        previous = None
        count = 1
        while current and count < position:
            previous = current
            current = current.next
            count += 1
        if not current:
            print("Position out of range.")
            return
        print(f"Deleted {current.data} from position {position}.")
        previous.next = current.next

    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        position = 1
        while current:
            if current.data == key:
                print(f"Element {key} found at position {position}.")
                return
            current = current.next
            position += 1
        print(f"Element {key} not found in the list.")

# Menu-driven interface
if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\n--- Linked List Operations Menu ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete from Beginning")
        print("5. Delete from End")
        print("6. Delete Node by Value")
        print("7. Delete Node by Position")
        print("8. Display List")
        print("9. Search for an Element")
        print("10. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            ll.insert_at_end(data)
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert: "))
            ll.insert_at_position(data, position)
        elif choice == 4:
            ll.delete_from_beginning()
        elif choice == 5:
            ll.delete_from_end()
        elif choice == 6:
            key = int(input("Enter the value of the node to delete: "))
            ll.delete_node(key)
        elif choice == 7:
            position = int(input("Enter position of the node to delete: "))
            ll.delete_at_position(position)
        elif choice == 8:
            ll.display()
        elif choice == 9:
            key = int(input("Enter the value to search: "))
            ll.search(key)
        elif choice == 10:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
