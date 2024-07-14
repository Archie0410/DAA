class Solution(object):
    def sortEvenOdd(self, nums):
        even = sorted([nums[i] for i in range(len(nums)) if i % 2 == 0])
        odd = sorted([nums[i] for i in range(len(nums)) if i % 2!= 0], reverse=True)
        result = []
        for e, o in zip(even, odd):
            result.append(e)
            result.append(o)
        if len(even) > len(odd):
            result.append(even[-1])
        elif len(odd) > len(even):
            result.append(odd[-1])
        return result
    