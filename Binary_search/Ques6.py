class Solution(object):
    def countNegatives(self, grid):
    
        m, n = len(grid), len(grid[0])
        count = 0
        j = n - 1

        for i in range(m):
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            count += (n - 1 - j)

        return count