#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start

valid_dig_ipv6 = list('1234567890ABCDEFabcdef')

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP: # this is either ipv4 or nothing
            str_list = queryIP.split('.')
            if len(str_list) != 4:
                return "Neither"
            for num_str in str_list:
                if not str.isdigit(num_str):
                    return "Neither"
                if len(num_str) == 0:
                    return "Neither"
                if num_str[0] == '0' and len(num_str) > 1:
                    return "Neither"
                num = int(num_str)
                if num < 0 or num > 255:
                    return "Neither"
            return "IPv4"

        if ':' in queryIP:
            str_list = queryIP.split(':')
            if len(str_list) != 8:
                return "Neither"
            for num_str in str_list:
                if len(num_str) > 4 or len(num_str) <= 0:
                    return "Neither"
                for c in num_str:
                    if c not in valid_dig_ipv6:
                        return "Neither"


            return "IPv6"


        return "Neither"


        
# @lc code=end

