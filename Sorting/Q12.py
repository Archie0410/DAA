class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] + prices[j] <= money:
                    return money - prices[i] - prices[j]
        return money