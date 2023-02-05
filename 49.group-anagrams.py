#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## do i assume each letter will happen at most once?
        def convert_word(s:str)->int:
            res = 0
            for c in s:
                res += 5**(ord(c) - ord('a'))
            return res
        my_dict = {}
        for s in strs:
            my_dict[convert_word(s)] = my_dict.get(convert_word(s), []) + [s]
        res = []
        for  val in my_dict.values():
            res.append(val)

        return res
# @lc code=end

