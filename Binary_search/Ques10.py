class Solution(object):
    def mySqrt(self, x):
        if x < 0:
            raise ValueError("Input should be a non-negative integer.")
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            curr_square = mid * mid
            if curr_square == x:
                return mid
            elif curr_square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
x = 16
solution = Solution()
result = solution.mySqrt(x)
print("Square root of", x, "is:", result)

x = 8
solution = Solution()
result = solution.mySqrt(x)
print("Square root of", x, "is:", result)