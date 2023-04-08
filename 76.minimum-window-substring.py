#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        missing = len(t)

        i = 0
        left, right = -1, -1
        for j, c in enumerate(s, 1):
            if t_count.get(c, 0) > 0:
                missing -= 1
            t_count[c] = t_count.get(c, 0) - 1

            if missing == 0:
                while i < j and t_count.get(s[i], 0) < 0:
                    t_count[s[i]] += 1
                    i += 1
                if right == -1 or j-i < right-left:
                    left, right = i, j
                t_count[s[i]] = t_count.get(s[i], 0) + 1
                missing += 1
                i += 1

        return s[left:right]
            





        from collections import Counter
        t_count = Counter(t)
        missing = len(t)
        i = 0
        left, right = -1, -1
        for j, c in enumerate(s, 1):
            if t_count[c] > 0:
                missing -= 1
            t_count[c] -= 1
             
            if missing == 0:
                while i < j and t_count[s[i]] < 0:
                    t_count[s[i]] += 1
                    i += 1

                if right == -1 or j-i < right - left:
                    left, right = i, j
                t_count[s[i]] += 1
                missing += 1
                i += 1

        return s[left:right]


        # from collections import Counter
        # t_count = Counter(t)
        # missing = len(t)
        # left, right = 0, 0
        # i = 0
        # for j, char in enumerate(s, 1):
        #     if t_count[char] > 0:
        #         missing -= 1
        #     t_count[char] -= 1
        #     if missing == 0:
        #         while i < j and t_count[s[i]] < 0:
        #             tmp = s[i]
        #             t_count[tmp] += 1
        #             # t_count[s[i]] += 1
        #             i += 1
        #         tmp = s[i]
        #         t_count[tmp] += 1
        #         missing += 1
        #         if right == 0 or j-i < right - left:
        #             left, right = i, j
        #         i += 1
        # return s[left:right]




        # greedy method : wrong
        # n_s = len(s)
        # n_t = len(t)
        # if n_t == 0:
        #     return ""
        # if n_s < n_t:
        #     return ""
        # s_count = {}
        # t_count = {}
        # for c in s:
        #     s_count[c] = s_count.get(c, 0) + 1
        # for c in t:
        #     t_count[c] = t_count.get(c, 0) + 1

        # for c in "ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghijklmnopqrstuvwxyz":
        #     if s_count.get(c, 0) < t_count.get(c, 0):
        #         return ""
            
        # # else there's a solution
        # left = 0
        # right = n_s - 1
        # while(True):
        #     if s_count.get(s[left], 0) > t_count.get(s[left], 0):
        #         s_count[s[left]]-=1
        #         left += 1
        #         continue
        #     if s_count.get(s[right], 0) > t_count.get(s[right], 0):
        #         s_count[s[right]]-=1
        #         right -= 1
        #         continue
        #     break
        # return s[left:right+1]

# @lc code=end

