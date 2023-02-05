#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check_eff_num(s:str):
            if len(s) <= 0 or len(s) > 3:
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            num_ = int(s)
            if num_ < 0 or num_ > 255:
                return False
            return True
        def restore_helper(s:str, n:int):
            if n > len(s):
                return []
            if n == 0:
                return []
            if n == 1:
                if check_eff_num(s):
                    return [s]
                return []
            res = []
            for dig in range(1, min(4, len(s)+1)):
                first_str = s[:dig]
                if not check_eff_num(first_str):
                    continue
                second_part = restore_helper(s[dig:], n-1)
                if len(second_part) == 0:
                    continue
                res += [first_str + '.' + x for x in second_part]
            return res

        return restore_helper(s, 4)

# @lc code=end

