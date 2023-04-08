def mergeArrays (nums1: list, nums2:list) -> list:
    n_1 = len(nums1)
    n_2 = len(nums2)
    i, j = 0, 0
    res = []
    while (i < n_1) and (j < n_2):
        idx_1 = nums1[i][0]
        idx_2 = nums2[j][0]
        if idx_1 < idx_2:
            res.append([idx_1, nums1[i][1]])
            i += 1
            break
        if idx_1 > idx_2:
            res.append([idx_2, nums2[j][1]])
            j += 1
            break
        # idx_1 == idx_2
        res.append([idx_1, nums1[i][1] + nums2[j][1]])
        i += 1
        j += 1
    while(i < n_1):
        res.append([nums1[i][0],nums1[i][1]])
        i+=1
    while(j < n_2):
        res.append([nums2[j][0],nums2[j][1]])
        j+=1
        
    return res



if __name__ == '__main__':
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    print( mergeArrays(nums1, nums2))