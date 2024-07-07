# Leetcode 704.Binary Search using recursion

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.recursive_search(nums, 0, len(nums) - 1, target)
    
    def recursive_search(self, nums, left, right, target):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if target < nums[mid]:
            return self.recursive_search(nums, left, mid - 1, target)
        
        if target > nums[mid]:
            return self.recursive_search(nums, mid + 1, right, target)
        
        return mid