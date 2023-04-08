#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def __init__(self):
        self.cache = {}
        self.palin_cache = {x:True for x in "abcdefghijklmnopqrstuvwxyz"}
    
    
    def is_palindrome(self, tmp_s):
        if tmp_s in self.palin_cache:
            return self.palin_cache[tmp_s]
    
        left = 0
        right = len(tmp_s) -1
        while(left <= right):
            if tmp_s[left] != tmp_s[right]:
                self.palin_cache[tmp_s] = False
                return False
            left += 1
            right -=1 

        self.palin_cache[tmp_s] = True
        return True

    def partition(self, s: str) -> List[List[str]]:
        if s in self.cache:
            return self.cache[s]
        
        n = len(s)
        if n == 0:
            self.cache[s] = [[]]
            return [[]]
        ans_ = []
        for i in range(n):
            if self.is_palindrome(s[:i+1]):
                tmp_res = self.partition(s[i+1:])
                ans_ += [[s[:i+1]] + x for x in tmp_res]
        self.cache[s] = ans_
        return ans_
        
        
# @lc code=end

