def find_rotations(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] < arr[(i-1)%n]:
            return n - i
    return 0
arr = [15, 18, 2, 3, 6, 12]
result = find_rotations(arr)
print("The array has been rotated", result, "times.")

arr = [7, 9, 11, 12, 5]
result = find_rotations(arr)
print("The array has been rotated", result, "times.")