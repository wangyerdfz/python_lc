/*
 * @lc app=leetcode id=990 lang=cpp
 *
 * [990] Satisfiability of Equality Equations
 */

// @lc code=start
class Solution {
public:
    int parent[26]; // parent
    bool equationsPossible(vector<string>& equations) {
        for(int i = 0; i < 26; ++i){
            parent[i] = i;
        }
        for (string e: equations){
            if (e[1] == '='){
                union_(e[0] - 'a', e[3] - 'a');
            }
        }
        for(string e: equations){
            if (e[1] == '!'){
                if (find(e[0] - 'a') == find(e[3] - 'a')){
                    return false;
                }
            }
        }
        return true;
    }
    int find(int x){ // find root
        if (parent[x] != x){
            return find(parent[x]);
        }
        return x;
    }
    void union_(int x, int y){
        parent[find(x)] = find(y);
    }





    // int uf[26];
    // bool equationsPossible(vector<string>& equations) {
    //     for (int i = 0; i < 26; ++i) uf[i] = i;
    //     for (string e : equations)
    //         if (e[1] == '=')
    //             uf[find(e[0] - 'a')] = find(e[3] - 'a');
    //     for (string e : equations)
    //         if (e[1] == '!' && find(e[0] - 'a') == find(e[3] - 'a'))
    //             return false;
    //     return true;
    // }

    // int find(int x) {
    //     if (x != uf[x]) uf[x] = find(uf[x]);
    //     return uf[x];
    // }
};
// @lc code=end

