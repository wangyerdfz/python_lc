#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        if n <= 1:
            return True
        open_status = [False]*n
        cur_keys = [0]
        while(cur_keys):
            key = cur_keys.pop()
            if not open_status[key]: # open the room and get keys
                cur_keys += rooms[key]
                open_status[key] = True
        res = True
        for item in open_status:
            res = res and item
        return res
# @lc code=end

