#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        res = []
        INSERTED = False
        i = 0
        if intervals[0][0] > newInterval[0]: # do newInterval
            res.append(newInterval)
            INSERTED = True
        else:
            res.append(intervals[0])
            i=1

        while(i < n):
            interval_ = intervals[i]
            if (INSERTED is False) and newInterval[0] < interval_[0]:
                interval_ = newInterval
                INSERTED = True
            else:
                i+=1

            if interval_[0] > res[-1][1]:
                res.append(interval_)
            else:
                res[-1][1] = max(res[-1][1], interval_[1])

        if INSERTED is False:
            if newInterval[0] > res[-1][1]:
                res.append(newInterval)
            else:
                res[-1][1] = max(res[-1][1], newInterval[1])


        return res



# @lc code=end

