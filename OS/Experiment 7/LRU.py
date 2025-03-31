def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    print("\nExecuting LRU Page Replacement...\n")
    for page in pages:
        if page in memory:
            memory.remove(page)
        else:
            if len(memory) == capacity:
                memory.pop(0)
                page_faults += 1
            else:
                page_faults += 1
        memory.append(page)
        print(f"Page: {page} => Memory: {memory}")
    
    print("\nTotal Page Faults (LRU):", page_faults)

def lru_menu():
    while True:
        print("\n=== LRU PAGE REPLACEMENT MENU ===")
        print("1. Run LRU with Custom Input")
        print("2. Run LRU with Default Input")
        print("3. Exit")
        print("==================================")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            pages = list(map(int, input("Enter Page Reference String (space-separated): ").split()))
            capacity = int(input("Enter Number of Frames: "))
            lru_page_replacement(pages, capacity)
        elif choice == '2':
            pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
            capacity = 3
            print(f"\nUsing default: Pages = {pages}, Frames = {capacity}")
            lru_page_replacement(pages, capacity)
        elif choice == '3':
            print("Exiting LRU Menu.")
            break
        else:
            print("Invalid choice. Try again.")

lru_menu()
