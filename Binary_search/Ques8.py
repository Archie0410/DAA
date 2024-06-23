class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right if right >= 0 and nums[right] == target else -1

        return [find_first(nums, target), find_last(nums, target)]


# Driver code
nums = [5, 7, 7, 8, 8, 10]
target = 8
solution = Solution()
result = solution.searchRange(nums, target)
print("Range of", target, "in the array is:", result)

nums = [5, 7, 7, 8, 8, 10]
target = 6
solution = Solution()
result = solution.searchRange(nums, target)
print("Range of", target, "in the array is:", result)