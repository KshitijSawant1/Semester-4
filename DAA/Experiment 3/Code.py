def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def menu():
    while True:
        print("\nQuick Sort - Menu")
        print("1. Enter an array")
        print("2. Sort using Quick Sort")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            global arr
            arr = list(map(int, input("Enter the numbers separated by space: ").split()))
            print("Array stored successfully!")
        elif choice == 2:
            if 'arr' in globals():
                quick_sort(arr, 0, len(arr) - 1)
                print("Sorted Array:", arr)
            else:
                print("Please enter an array first (Option 1).")
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again!")

# Run Menu
menu()
