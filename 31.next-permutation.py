#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return 
        if n == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        
        for k in range(n-2, -1, -1):
            if nums[k + 1] > nums[k]:
                break
        else: # if no break
            i = 0
            j = n - 1
            while(i <= j):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            return
        
        # now k would be the index that I need to swap, from the left find the smallest element thats bigger than nums[k] (first element)
        for j in range(n - 1, k, -1):
            if nums[j] > nums[k]:
                nums[k], nums[j] = nums[j], nums[k]
                break

        # reverse all the element up to k
        i = k+1
        j = n-1
        while(i <= j):
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1

        return
        # def nextPermutationHelper(nums: List[int], begin, end):
        #     """
        #     if returns True: no changes needs to be made
        #     if returns False: cannot find a next, needs another layer of operation
        #     """
        #     # if begin + 1 == end:
        #     #     nums[end], nums[begin] = nums[begin], nums[end]
        #     #     if nums[begin] > nums[end]:
        #     #         return True
        #     #     return False

                
        #     if begin == end:
        #         return False

        #     res = nextPermutationHelper(nums, begin+1, end)
        #     if res :
        #         return res
        #     else:  # res == False
        #         # i = begin + 1
        #         # j = end
        #         # while i < j:
        #         #     nums[i], nums[j] = nums[j], nums[i]
        #         #     i += 1
        #         #     j -= 1
                
        #         i = begin + 1
        #         while i <= end:
        #             if nums[i] > nums[begin]:
        #                 nums[begin], nums[i] = nums[i], nums[begin]
        #                 return True
        #             i+=1
        #         for i in range(begin + 1, end + 1):
        #             nums[i - 1], nums[i] = nums[i], nums[i - 1]
        #         return False

        # n = len(nums)
        # if n<=1:
        #     return 
        # nextPermutationHelper(nums, 0, n-1)
        # return
        

        
# @lc code=end

