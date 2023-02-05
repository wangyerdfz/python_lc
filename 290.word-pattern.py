#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        map_fwd = {}
        map_bcwd = {}
        for i in range(len(pattern)):
            if pattern[i] in map_fwd.keys():
                if map_fwd[pattern[i]] != s_list[i]:
                    return False
            if s_list[i] in map_bcwd.keys():
                if map_bcwd[s_list[i]] != pattern[i]:
                    return False
            map_fwd[pattern[i]] = s_list[i]
            map_bcwd[s_list[i]] = pattern[i]

        return True



# def wordPattern( pattern: str, s: str) -> bool:
#     s_list = s.split()
#     print()
#     if len(s_list) != len(pattern):
#         return False
#     map_fwd = {}
#     map_bcwd = {}
#     for i in range(len(pattern)):
#         print(map_fwd)
#         print(map_bcwd)
#         if pattern[i] in map_fwd.keys():
#             if map_fwd[pattern[i]] != s_list[i]:
#                 return False
#         if s_list[i] in map_bcwd.keys():
#             if map_bcwd[s_list[i]] != pattern[i]:
#                 return False
#         map_fwd[pattern[i]] = s_list[i]
#         map_bcwd[s_list[i]] = pattern[i]

#     return True


# if __name__ == '__main__':
#     print(wordPattern("abba", "dog cat cat dog"))

# @lc code=end

