def bubble_sort(arr):
    """Bubble Sort Algorithm to sort the array"""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements

def binary_search(arr, low, high, key):
    """Recursive Binary Search Function"""
    if low > high:
        return -1  # Element not found
    
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid  # Element found
    elif key < arr[mid]:  # Search in the left half
        return binary_search(arr, low, mid - 1, key)
    else:  # Search in the right half
        return binary_search(arr, mid + 1, high, key)

def menu():
    """Menu-Driven Program for Binary Search"""
    while True:
        print("\nBinary Search Menu")
        print("1. Enter an array")
        print("2. Search for an element")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            global arr
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Array stored successfully!")
        
        elif choice == 2:
            if 'arr' in globals():
                key = int(input("Enter the element to search: "))
                
                # Sort the array using Bubble Sort
                print("Sorting the array using Bubble Sort...")
                bubble_sort(arr)
                print("Sorted Array:", arr)

                # Perform Binary Search
                index = binary_search(arr, 0, len(arr) - 1, key)
                
                if index != -1:
                    print(f"Element found at index: {index}")
                else:
                    print("Element not found.")
            else:
                print("Please enter an array first (Option 1).")

        elif choice == 3:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

# Run Menu
menu()
