import collections

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).



class Solution(object):
    def maxProfit(self, prices):
        buy = True
        sell = False
        profit = 0
        buyingPrice = 0
        for i in range(len(prices)):
            if i != len(prices)-1 and prices[i] < prices[i+1] and buy:
                buyingPrice = prices[i]
                sell = True
                buy = False
            elif ((i != len(prices)-1 and prices[i] > prices[i+1]) or (i == len(prices)-1)) and sell:
                sellingPrice = prices[i]
                profit += sellingPrice - buyingPrice
                sell = False
                buy = True
            else: continue

        return profit


if __name__ == '__main__':

    arr = [1,2,1,2,1,2]
    solution = Solution()
    print(solution.maxProfit(arr))