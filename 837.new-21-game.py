#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
            
        probs = [0]*(k + maxPts)
        probs[0] = 1
        probs[1] = 1/maxPts
        for i in range(2, k + maxPts):
            if i <= k:
                if i >= maxPts + 1:
                    probs[i] = (1 + maxPts) / maxPts * probs[i-1] - 1/maxPts*probs[i-1-maxPts]
                else:
                    probs[i] = probs[i-1]*(1  + 1/maxPts)
            else:
                probs[i] =  probs[i-1] - 1/maxPts*probs[i-1-maxPts]
        res = 0
        for i in range(n+1, maxPts + k):
            res += probs[i]

        return 1 - res
# @lc code=end

