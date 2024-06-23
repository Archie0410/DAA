class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1
n = 10
solution = Solution()
result = solution.guessNumber(n)

print("The number I picked is", result)