#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def __init__(self):
        self.scrambles = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.scrambles:
            return self.scrambles[(s1, s2)]
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2:
            self.scrambles[(s1, s2)] = False
            return False
        if sorted(s1) != sorted(s2):
            self.scrambles[(s1, s2)] = False
            return False
        if n1 == 0:
            self.scrambles[(s1, s2)] = True
            return True
        if n1 == 1:
            self.scrambles[(s1, s2)] = (s1 == s2)
            return s1 == s2
        if n1 == 2:
            self.scrambles[(s1, s2)] = (s1 == s2) or (s1[1] + s1[0] == s2)
            return (s1 == s2) or (s1[1] + s1[0] == s2)
        for i in range(1, n1):
            if i < n1 - i:
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                    self.scrambles[(s1, s2)] = True
                    return True
                if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                    self.scrambles[(s1, s2)] = True
                    return True
            else:
                if  self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
                    self.scrambles[(s1, s2)] = True
                    return True
                if  self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[:i], s2[-i:]):
                    self.scrambles[(s1, s2)] = True
                    return True
        self.scrambles[(s1, s2)] = False
        return False
            

        
# @lc code=end

