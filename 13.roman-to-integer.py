#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        sum_ = 0
        i = 0
        while(i < n):
            if s[i] == 'I':
                if (i < n - 1) and (s[i + 1] == 'V'):
                    sum_ += 4
                    i += 2
                    continue
                if (i < n - 1) and (s[i + 1] == 'X'):
                    sum_ += 9
                    i += 2
                    continue
                sum_ += 1
                i += 1
                continue
            if s[i] == 'X':
                if (i < n - 1) and (s[i + 1] == 'L'):
                    sum_ += 40
                    i += 2
                    continue
                if (i < n - 1) and (s[i + 1] == 'C'):
                    sum_ += 90
                    i += 2
                    continue
                sum_ += 10
                i += 1
                continue
            if s[i] == 'C':
                if (i < n - 1) and (s[i + 1] == 'D'):
                    sum_ += 400
                    i += 2
                    continue
                if (i < n - 1) and (s[i + 1] == 'M'):
                    sum_ += 900
                    i += 2
                    continue
                sum_ += 100
                i += 1
                continue
            if s[i] == 'V':
                sum_ += 5
                i += 1
                continue
            if s[i] == 'L':
                sum_ += 50
                i += 1
                continue
            if s[i] == 'D':
                sum_ += 500
                i += 1
                continue
            if s[i] == 'M':
                sum_ += 1000
                i += 1
                continue

        return sum_
# @lc code=end

