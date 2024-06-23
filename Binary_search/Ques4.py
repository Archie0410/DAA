# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        h=n
        while l<=h:
            m=(l+h)//2
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                h=m-1
            else:
                l=m+1