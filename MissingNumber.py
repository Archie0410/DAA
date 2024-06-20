class Solution(object):
    def missingNumber(self, nums):
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i
            result ^= num
        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 3]
    missing_number = solution.missingNumber(nums)
    print("The missing number is:", missing_number)

    