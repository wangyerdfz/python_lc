def integerBreak(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    res_multiple = [0] * n
    res_single = [n-i for i in range(n)]
    res_multiple[-1] = 1
    res_multiple[-2] = 1
    for i in range(n-3, -1, -1):
        max_ = 0
        for j in range(i + 1, n):
            max_ = max(max_, (j-i)*max(res_multiple[j], res_single[j]))
        res_multiple[i] = max_
    return res_multiple[0]


if __name__ == '__main__':
    integerBreak(4)