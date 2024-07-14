class Solution(object):
    def numberGame(self, nums):
        arr = []
        while nums:
            alice_min = min(nums)
            nums.remove(alice_min)
            bob_min = min(nums)
            nums.remove(bob_min)
            arr.append(bob_min)
            arr.append(alice_min)
        return arr