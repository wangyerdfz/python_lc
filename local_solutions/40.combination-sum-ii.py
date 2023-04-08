def combinationSum2( candidates: list[int], target: int):
    def comb_help(useable_cand : list, cand_count :dict, target : int):
        if target == 0:
            return [[]]
        if target < 0:
            return []
        
        n = len(useable_cand)

        cur_max = 0

        for i in useable_cand:
            cur_max += i * cand_count.get(i, 0)
        if n <= 0 or cur_max < target:
            return []
        res = []

        if cand_count.get(useable_cand[0], 0) > 0:
            tmp_count = cand_count.copy()
            tmp_count[useable_cand[0]] -= 1
            res += [[useable_cand[0]] + x for x in comb_help(useable_cand, tmp_count, target - useable_cand[0])]
        res += comb_help(useable_cand[1:], cand_count.copy(), target)

        return res

    count_ = {}
    for i in candidates:
        count_[i] = count_.get(i, 0) + 1

    cand = list(count_.keys())
    cand.sort()

    return comb_help(cand, count_, target)


if __name__ == '__main__':
    cand = [10,1,2,7,6,1,5]
    target = 8
    print(combinationSum2(cand, target))