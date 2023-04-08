def search(nums: list[int], target: int) -> int:
    n = len(nums)
    if n  == 0:
        return -1
    if n == 1 :
        if nums[0] == target:
            return 0
        else:
            return 1
    def access_val(idx):
        return nums[(idx + n)%n]
        
    # use log n to find the minimum
    min_idx = -1
    left = 0
    right = n-1

# find min
    while(left < right):
        if access_val(left-1) > access_val(left):
            min_idx = left
            break
        elif access_val(right-1) > access_val(right):
            min_idx = right
            break
        mid = left + (right - left) // 2
        if access_val(mid-1) > access_val(mid):
            min_idx = mid
            break
        if access_val(mid) > access_val(left): # min on the right side
            left = mid + 1
        else:
            right = mid




    low = 0
    high = n - 1

    while(low < high):
        mid = low + (high - low) //2
        if nums[(mid + min_idx)%n] == target:
            return (mid + min_idx)%n
        if nums[(mid + min_idx)%n] > target:
            high = mid
        else:
            low = mid + 1
    if ( low == high) and (nums[(low+ min_idx)%n] == target):
        return (low+ min_idx)%n
    return -1


if __name__ == '__main__':
    nums_  = [4, 5, 6, 7, 0, 1, 2]
    target_ = 0
    print(search(nums_, target_))