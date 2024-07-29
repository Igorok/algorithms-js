def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pi_left, pi_right = partition(arr, low, high)

        # Recursively sort elements before partition and after partition
        quick_sort(arr, low, pi_left - 1)
        quick_sort(arr, pi_right + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low
    right = high
    i = low

    while i <= right:
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] > pivot:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
        else:
            i += 1

    return left, right

# Example usage:
arr = [10, 7, 8, 9, 1, 5, 9, 9, 5, 10]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
