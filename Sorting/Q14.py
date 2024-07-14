class Solution(object):
    def frequencySort(self, nums):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        nums.sort(key=lambda x: (count[x], -x))
        return nums