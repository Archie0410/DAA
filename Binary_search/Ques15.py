def find_rotations(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low

arr = [15, 18, 2, 3, 6, 12]
result = find_rotations(arr)
print("The array has been rotated", result, "times.")

arr = [7, 9, 11, 12, 5]
result = find_rotations(arr)
print("The array has been rotated", result, "times.")