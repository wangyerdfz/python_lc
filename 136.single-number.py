#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:



def prob(N):
    probs = [0] * N
    probs[0] = 1/6
    if N <= 6:
        for i in range(1, N):
            probs[i] = 1 / 6
            for j in range(0, i):
                probs[i] += 1/6 * probs[j]
    else:
        for i in range(1, 6):
            probs[i] = 1 / 6
            for j in range(0, i):
                probs[i] += 1/6 * probs[j]
        for i in range(6, N):
            probs[i] = 1/6 * sum(probs[i - 6 : i])

    for i, p in enumerate(probs):
        print(f'{i + 1} : {p}')
    print(sum(probs[:6])/6)

if __name__ == '__main__':
    prob(100)
        
# @lc code=end

