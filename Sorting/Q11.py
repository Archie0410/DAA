class Solution(object):
    def specialArray(self, nums):
        nums.sort(reverse=True)
        for i, x in enumerate(nums, 1):
            if x >= i:
                if i == len(nums) or nums[i] < i:
                    return i
        return -1