class Solution(object):
    def arrangeCoins(self, n):
        k = 1
        while n >= k:
            n -= k
            k += 1
        return k - 1