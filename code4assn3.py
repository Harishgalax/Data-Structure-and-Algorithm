def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Elements smaller than the pivot
        smaller = [elem for elem in arr[1:] if elem <= pivot]
        # Elements greater than the pivot
        greater = [elem for elem in arr[1:] if elem > pivot]
        
        # Recursively sort the smaller and greater elements
        return quick_sort(smaller) + [pivot] + quick_sort(greater)

# Example usage:
arr = [12, 4, 5, 6, 7, 3, 1, 15]
print("Original array:", arr)

arr = quick_sort(arr)

print("Sorted array:", arr)