def removeDuplicates( nums) -> int:
    n = len(nums)
    if n <= 1:
        return n
    swap_idx = -1

    idx = 0
    cur_num = nums[idx]
    cnt = 1
    for idx in range(1, n):
        if nums[idx] == cur_num:
            if swap_idx == -1:
                swap_idx = idx

        else: # new number
            if swap_idx == -1: # dont do anything
                cnt+=1
            else:
                nums[swap_idx] = nums[idx]
                swap_idx +=1
                cur_num = nums[idx]
                cnt+=1

    return cnt

if __name__ == '__main__':
    