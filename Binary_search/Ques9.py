class Solution(object):
    def isPerfectSquare(self, num):
        if num < 2:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            curr_square = mid * mid
            if curr_square == num:
                return True
            elif curr_square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
num = 16
solution = Solution()
result = solution.isPerfectSquare(num)
print(num, "is a perfect square:", result)

num = 14
solution = Solution()
result = solution.isPerfectSquare(num)
print(num, "is a perfect square:", result)