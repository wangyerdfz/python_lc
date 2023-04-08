def minWindow( s: str, t: str) -> str:
    n_s = len(s)
    n_t = len(t)
    if n_t == 0:
        return ""
    if n_s < n_t:
        return ""
    s_count = {}
    t_count = {}
    for c in s:
        s_count[c] = s_count.get(c, 0) + 1
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1

    for c in "ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghijklmnopqrstuvwxyz":
        if s_count.get(c, 0) < t_count.get(c, 0):
            return ""
        
    # else there's a solution
    left = 0
    right = n_s - 1
    while(True):
        if s_count.get(s[left], 0) > t_count.get(s[left], 0):
            s_count[s[left]] -=1
            left += 1
            print(left)
            continue
        if s_count.get(s[right], 0) > t_count.get(s[right], 0):
            s_count[s[right]] -=1
            right -= 1
            continue

        break
    return s[left:right+1]



if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))