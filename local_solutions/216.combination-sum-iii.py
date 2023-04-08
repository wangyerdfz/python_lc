def combinationSum3( k: int, n: int):
    def comb_helper(k_, sum_, start):
        
        res = []
        if k_ == 1:
            if sum_ >= start and sum_ <= 9:
                return [[sum_]]
            return res

        if k_> (9 - start + 1):
            return res
        sum_min = 0
        for i in range(k_):
            sum_min += start + i
        sum_max = 0
        for i in range(k_):
            sum_max += 9 - i
        if sum_ < sum_min or sum_ > sum_max:
            return res
        for i in range(start, 10):
            next_comb = comb_helper(k_-1, sum_-i, i+1)
            if len(next_comb) > 0:
                res += [[i] + x for x in next_comb]
        
        return res
    return comb_helper(k, n, 1)


if __name__ == '__main__':
    print(combinationSum3(3, 7))