def minOperations( n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    i = 1
    while(2**i < n):
        i+=1
    if 2**i == n:
        return 1
    res_array = [-1]*(2**i + 1)
    for j in range(i+1):
        res_array[2**j] = 1
    res_array[0] = 0
    cut_off = 1
    while(cut_off <= i):
        for idx in range(2**(cut_off-1) + 1, 2**(cut_off) + 1):
            res_array[idx] = min(res_array[2**(cut_off-1)] + res_array[idx - 2**(cut_off-1)], res_array[2**(cut_off)]+ res_array[2**(cut_off)- idx])
        cut_off += 1
            
    return res_array[n]


if __name__ == '__main__':
    n = 39
    print(minOperations(n))