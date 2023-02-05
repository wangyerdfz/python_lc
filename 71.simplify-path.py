#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        tokens are of the following format [type, value]
        type can be slash, dot, path_name
        values in shash is None, it can only have a single slash
        values in dot could be '.' or '..'
        values in path_name is a path name, it cannot contain slash '/'

        """
        def tokenize(path):
            def make_token(s):
                if len(s) <= 0:
                    return None
                if s == '.':
                    return ['dot', '.']
                if s == '..':
                    return ['dot', '..']

                return ['path_name', s]
            res = path.split("/")
            return [make_token(x) for x in res if len(x) > 0]
        

        tokens = tokenize(path)
        res = []
        for token in tokens:
            if token[0] == 'dot':
                if token[1] == '..':
                    if res:
                        res.pop()
                # else : "." or ".." at root, dont do anything

            else: # token[0] = path:
                res.append(token[1])

        # conversion:
        if len(res) == 0:
            return '/'
        
        res_str = ""
        for path_ in res:
            res_str += ("/" + path_)

        return res_str
        
                
                


        
# @lc code=end

