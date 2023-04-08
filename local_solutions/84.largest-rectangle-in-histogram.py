def largestRectangleArea(heights: list) -> int:
    import numpy as np
    # worse case scenario: use o n^2 to get the lowest
    n = len(heights)
    
    if n <= 0:
        return 0
    if n == 1:
        return 
    min_num = np.zeros((n, n),dtype=int)
    for i in range(n):
        min_num[i, i] = heights[i]
    for i in range(n):
        for j in range(i+1, n):
            if heights[j] < min_num[i, j-1]:
                min_num[i, j] = heights[j]
            else:
                min_num[i, j] = min_num[i, j-1]

    max_ = -1
    for i in range(n):
        for j in range(i, n):
            if min_num[i, j] * (j-i+1) > max_:
                max_ = min_num[i, j] * (j-i+1)
    return max_


if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))