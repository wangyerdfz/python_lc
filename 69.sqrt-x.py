#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        ERROR = 1e-6
        if x == 1:
            return 1
        pre = 1
        pos = 5
        while( pos - pre > ERROR or pos - pre < -ERROR):
            pre, pos = pos, 1/2*(pos + x / pos)
            # pre, pos = pos, 3/4*pos + x**2 / 4 / pos**3
            
        res = math.ceil(pos)
        if res * res > x :
            return res - 1
        return res


# def mySqrt(x: int) -> int:
#     high = x
#     low = 1
#     while(low < high):

#         mid = low + (high - low)//2
#         print(f"low {low}, high {high}, mid {mid}")
#         if mid**2 < x:
#             print(f'mid too low')
#             low = mid + 1
#         elif mid**2 > x:
#             print(f'mid too high')
#             high = mid
#         else:
#             print(f'found exact solution')
#             return mid
#     if low**2 > x :
#         return low - 1
#     return low

# if __name__ == '__main__':
#     print(mySqrt(8))
# @lc code=end

