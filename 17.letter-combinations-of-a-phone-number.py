#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
DIGIT_DICT = {"2" : "abc",
              "3" : "def",
              "4" : "ghi",
              "5" : "jkl",
              "6" : "mno",
              "7" : "pqrs",
              "8" : "tuv",
              "9" : "wxyz"}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []
        if len(digits) == 1:
            return [x for x in DIGIT_DICT[digits]]
        temp_list = []
        for char in DIGIT_DICT[digits[0]]:
            temp_list += [char + x for x in self.letterCombinations(digits[1:])]
        return temp_list

# @lc code=end

