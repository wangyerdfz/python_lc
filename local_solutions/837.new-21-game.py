def new21Game(n: int, k: int, maxPts: int) -> float:
    probs = [0]*(k + maxPts)
    probs[0] = 1
    probs[1] = 1/maxPts
    for i in range(2, k + maxPts):
        if i <= k:
            if i >= maxPts + 1:
                probs[i] = (1 + maxPts) / maxPts * probs[i-1] - 1/maxPts*probs[i-1-maxPts]
            else:
                probs[i] =  (1 + maxPts)/maxPts*probs[i-1] 
        else:
            probs[i] =  probs[i-1] - 1/maxPts*probs[i-1-maxPts]
    res = 0
    for i in range(n+1, maxPts + k):
        res += probs[i]

    return 1 - res



if __name__ == '__main__':
    print(new21Game(21, 17, 10))