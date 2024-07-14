class Solution(object):
    def findDuplicates(self, nums):
      
        duplicates = []
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num - 1] < 0:
                duplicates.append(abs_num)
            else:
                nums[abs_num - 1] *= -1
        return duplicates