#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def count_say(s)->str:
            len_ = len(s)
            if len_ == 0:
                return ""
            type_ = s[0]
            count_ = 1
            for i in range(1, len_):
                if s[i] != type_:
                    break
                count_ += 1

            return str(count_) + type_ + count_say(s[count_:])

        if n == 0:
            return ""
        if n == 1:
            return "1"
        return count_say(self.countAndSay(n-1))
        
# @lc code=end

