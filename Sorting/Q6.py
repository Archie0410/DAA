class Solution(object):
    def kWeakestRows(self, mat, k):
        soldiers = [(row.count(1), i) for i, row in enumerate(mat)]
        soldiers.sort()
        return [i for _, i in soldiers[:k]]