"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        valley = prices[0]
        peak = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]: #then it is new peak
                peak = prices[i]
                if i == len(prices) - 1:
                    max_profit += peak - valley
            else: #then it is new valley
                max_profit += peak - valley
                valley = prices[i]
                peak = valley
        return max_profit
    
if __name__ == '__main__':
    s = Solution()
   
    # Test case 1
    prices1 = [7,1,5,3,6,4]
    expecxted_output1 = 7
    k = s.maxProfit(prices1)
    assert k == expecxted_output1, f"Test Case 1 Failed: expected output {expecxted_output1}, but got {k}"

    # Test case 2
    prices2 = [1,2,3,4,5]
    expecxted_output2 = 4
    k = s.maxProfit(prices2)
    assert k == expecxted_output2, f"Test Case 2 Failed: expected output {expecxted_output2}, but got {k}"

    # Test case 3
    prices3 = [7,6,4,3,1]
    expecxted_output3 = 0
    k = s.maxProfit(prices3)
    assert k == expecxted_output3, f"Test Case 3 Failed: expected output {expecxted_output3}, but got {k}"