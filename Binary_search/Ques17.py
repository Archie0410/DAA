class Solution(object):
    def findKthPositive(self, arr, k):
        i, num = 0, 1
        while True:
            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                k -= 1
                if k == 0:
                    return num
            num += 1