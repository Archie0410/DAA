def find_floor_ceil(arr, target):
    n = len(arr)
    floor = -1
    ceil = -1

    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            floor = ceil = mid
            break
        elif arr[mid] < target:
            floor = mid
            low = mid + 1
        else:
            ceil = mid
            high = mid - 1

    return floor, ceil
arr = [1, 2, 3, 4, 8, 10, 12, 19]
target = 5

floor, ceil = find_floor_ceil(arr, target)

if floor!= -1:
    print("Floor of", target, "is", arr[floor])
else:
    print("Floor of", target, "does not exist")

if ceil!= -1:
    print("Ceil of", target, "is", arr[ceil])
else:
    print("Ceil of", target, "does not exist")