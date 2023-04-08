def threeSum( nums: list) -> list:
    res = []
    nums.sort()
    n = len(nums)
    res = []

    if n <=2:
        return res

    pos_dict = {}
    for idx, i in enumerate(nums):
            pos_dict[i] = idx

    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i-1] == nums[i]:
            continue
        for j in range(i+1, n):
            if nums[i] + 2*nums[j] > 0:
                return res
            if j > i+1 and nums[j-1] == nums[j]:
                continue
            if -nums[i]-nums[j] in pos_dict:
                if pos_dict[-nums[i]-nums[j]] > j:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])

    return res


if __name__ == '__main__':
    print(threeSum([3,0,-2,-1,1,2]))