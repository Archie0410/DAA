class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left % len(letters)]
letters = ["c", "f", "j"]
target = "a"
solution = Solution()
result = solution.nextGreatestLetter(letters, target)
print("The smallest character that is lexicographically greater than", target, "is:", result)

letters = ["c", "f", "j"]
target = "c"
solution = Solution()
result = solution.nextGreatestLetter(letters, target)
print("The smallest character that is lexicographically greater than", target, "is:", result)

letters = ["c", "f", "j"]
target = "d"
solution = Solution()
result = solution.nextGreatestLetter(letters, target)
print("The smallest character that is lexicographically greater than", target, "is:", result)

letters = ["c", "f", "j"]
target = "g"
solution = Solution()
result = solution.nextGreatestLetter(letters, target)
print("The smallest character that is lexicographically greater than", target, "is:", result)