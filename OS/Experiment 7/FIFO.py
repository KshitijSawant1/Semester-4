def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    print("\nExecuting FIFO Page Replacement...\n")
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        print(f"Page: {page} => Memory: {memory}")
    
    print("\nTotal Page Faults (FIFO):", page_faults)

def fifo_menu():
    while True:
        print("\n=== FIFO PAGE REPLACEMENT MENU ===")
        print("1. Run FIFO with Custom Input")
        print("2. Run FIFO with Default Input")
        print("3. Exit")
        print("===================================")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            pages = list(map(int, input("Enter Page Reference String (space-separated): ").split()))
            capacity = int(input("Enter Number of Frames: "))
            fifo_page_replacement(pages, capacity)
        elif choice == '2':
            pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
            capacity = 3
            print(f"\nUsing default: Pages = {pages}, Frames = {capacity}")
            fifo_page_replacement(pages, capacity)
        elif choice == '3':
            print("Exiting FIFO Menu.")
            break
        else:
            print("Invalid choice. Try again.")

fifo_menu()
