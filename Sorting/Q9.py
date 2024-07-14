class Solution(object):
    def findRelativeRanks(self, score):
        sorted_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score) + 1)]
        return [ranks[sorted_score.index(i)] for i in score]