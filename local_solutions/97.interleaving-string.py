def isInterleave(s1: str, s2: str, s3: str) -> bool:
    def is_interleave_helper(s1, s2, s3):
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        if n2 == 0 and s1 == s3:
            return True
        if n1 == 0:
            return False
        ans = False
        for i in range(1,n1+1):
            ans = (ans or (s1[:i] == s3[:i] and is_interleave_helper(s2, s1[i:], s3[i:])))
            if ans:
                return True
        return False
    
    return is_interleave_helper(s1, s2, s3) or is_interleave_helper(s2, s1, s3)


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # print(isInterleave(s1, s2, s3))
    print(isInterleave("dbbca","bcc", "dbbcbcac"))
    # print(isInterleave( "c", "","c"))
    print(s1[:2] == s3[:2])