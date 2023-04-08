def squareFreeSubsets( nums: list) -> int:
    #step 1: take the unique set
    import numpy as np
    num_used = []
    for num in nums:
        if num not in [4, 8, 12, 16, 20, 24, 28, 9, 18, 27, 25]:
            num_used.append(num)
    n = len(num_used)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    decomp_table = np.zeros((31, len(primes)), dtype=int)
    for i in range(1, 31):
        tmp_num = i
        for prime_idx, prime in enumerate(primes):
            while(tmp_num%prime == 0):
                # print(tmp_num, prime)
                decomp_table[i, prime_idx] += 1
                tmp_num = tmp_num//prime
    counter_ = 1
    for counter in range(
    n = len(num_used)
    for i in num_used:
        counter_ += 1
        for j in range(i + 1, 31):
            if exist_num[j] != 1:
                continue
            default_ = 1
            for k in range(len(primes)):
                if decomp_table[i, k] + decomp_table[j, k] >= 2:
                    default_ = 0
            if default_ == 1:
                print(i, j)
            counter_ += default_
                    
                
        
    return counter_


if __name__ == '__main__':
    nums = [11,2,19,7,9,27]
    print(squareFreeSubsets(nums))