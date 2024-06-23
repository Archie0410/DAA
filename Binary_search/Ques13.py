class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
      
        left, right = 0, peak
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = peak, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
mountain_arr = MountainArray([1, 2, 3, 4, 5, 3, 1])
target = 3
solution = Solution()
result = solution.findInMountainArray(target, mountain_arr)
print("The minimum index such that mountainArr.get(index) == target is:", result)

mountain_arr = MountainArray([0, 1, 2, 4, 2, 1])
target = 3
solution = Solution()
result = solution.findInMountainArray(target, mountain_arr)
print("The minimum index such that mountainArr.get(index) == target is:", result)