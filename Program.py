def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage
arr = input("Enter the sorted array elements (space-separated): ").split()
arr = [int(num) for num in arr]
target = int(input("Enter the target element: "))

result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in the array")
