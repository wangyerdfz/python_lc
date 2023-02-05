#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return (nums2[len(nums2)//2] + nums2[(len(nums2) - 1)//2])/2
        if len(nums2) == 0:
            return (nums1[len(nums1)//2] + nums1[(len(nums1) - 1)//2])/2

        if (len(nums1) + len(nums2)) % 2 == 1:
            # only needs to find one number
            target = (len(nums1) + len(nums2))//2
            iter_1 = 0
            iter_2 = 0
            counter = -1
            num_ = 0
            while(counter < target):
                if (iter_1 >= len(nums1)):
                    num_ = nums2[iter_2]
                    iter_2+=1
                    counter+=1
                elif (iter_2 >= len(nums2)):
                    num_ = nums1[iter_1]
                    iter_1+=1
                    counter+=1
                elif nums1[iter_1] < nums2[iter_2]:
                    num_ = nums1[iter_1]
                    iter_1 += 1
                    counter+=1
                else:
                    num_ = nums2[iter_2]
                    iter_2 += 1
                    counter += 1
            return num_
        
        target = (len(nums1) + len(nums2))//2 - 1
        iter_1 = 0
        iter_2 = 0
        counter = -1
        num_ = 0
        num_1 = 0
        while(counter < target + 1 ):
            if (iter_1 >= len(nums1)):
                num_ = nums2[iter_2]
                iter_2+=1
                counter+=1
            elif (iter_2 >= len(nums2)):
                num_ = nums1[iter_1]
                iter_1+=1
                counter+=1
            elif nums1[iter_1] < nums2[iter_2]:
                num_ = nums1[iter_1]
                iter_1 += 1
                counter+=1
            else:
                num_ = nums2[iter_2]
                iter_2 += 1
                counter += 1
            if (counter == target):
                num_1 = num_
        return (num_1 + num_)/2


# O(log(n + n))? some sort of binary search way
        

# @lc code=end

