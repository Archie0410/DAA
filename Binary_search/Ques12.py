class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
nums = [1, 2, 3, 1]
solution = Solution()
result = solution.findPeakElement(nums)
print("The index of a peak element is:", result)

nums = [1, 2, 1, 3, 5, 6, 4]
solution = Solution()
result = solution.findPeakElement(nums)
print("The index of a peak element is:", result)