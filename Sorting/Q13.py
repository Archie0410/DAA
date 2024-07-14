class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        res = []
        for num in nums:
            res.append(sorted_nums.index(num))
        return res