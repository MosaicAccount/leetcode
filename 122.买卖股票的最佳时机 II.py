#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30404
#
# [122] 买卖股票的最佳时机 II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        i = 0
        j = 1
        res = 0

        while i <= j and  j < len(prices):

            if prices[i] > prices[j]:
                i += 1
                j += 1
                continue
            
            while j < len(prices) - 1 and prices[j] < prices[j + 1]:
                j+=1
            
            res += prices[j] - prices[i]
            i = j + 1
            j += 1
        
        return res


# @lc code=end


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#
