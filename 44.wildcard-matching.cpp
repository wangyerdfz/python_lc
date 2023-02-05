/*
 * @lc app=leetcode id=44 lang=cpp
 *
 * [44] Wildcard Matching
 */

// @lc code=start

class Solution {
public:
    bool isMatch(string s, string p){

        const int s_size = s.size();
        const int p_size = p.size();
        if (p_size == 0){
            return s_size == 0;
        }

        bool res[s_size + 1][p_size + 1];
        // initialize all to be false, though not completely necessary
        for( int i {0}; i < s_size + 1; ++i){
            for (int j {0}; j < p_size + 1; ++j){
                res[i][j] = false;
            }
        }
        res[s_size][p_size] = true;
        for(int i = 0; i < s_size; ++i){ // boundary conditions
            res[i][p_size] = false;
        }
        for(int i = p_size - 1; i >=0; --i){ // boundary set
            res[s_size][i] = (p[i] == '*') && (res[s_size][i + 1]);
        }
        for(int i = s_size - 1; i >= 0; --i){
            for (int j = p_size - 1; j >= 0; --j){
                if (p[j] == '*'){ // *
                    res[i][j] = (res[i + 1][j]) || (res[i][j + 1]);
                }
                else if (isalpha(p[j]) ){ // A-Za-z
                    res[i][j] = (p[j] == s[i]) && (res[i + 1][j + 1]);
                }
                else{ // ?
                    res[i][j] = (res[i + 1][j + 1]);
                }
            }
        }
        return res[0][0];






    //     if (p.size() == 0){
    //         return s.size() == 0;
    //     }
    //     bool res[s.size()][p.size()] {false};
    //     for(int p_iter { p.size() - 1}; p_iter >= 0; p_iter--){
    //         if (isalpha(p[p_iter])){
                
    //         }
    //     }
    // }
    
    // bool isMatch(string s, string p) {
    //     // need to trim the pattern string
    //     std::string new_p {""};
    //     if (p.size() <= 0){
    //         new_p = p;
    //     }
    //     else{
    //         new_p += p[0];
    //         for(int i {1}; i < p.size(); ++i){
    //             if (p[i] == '*' && p[i - 1] == '*'){
    //                 // do nothing
    //             }
    //             else{
    //                 new_p += p[i];
    //             }
    //         }
    //     }
        

    //     return isMatchHelper(s, new_p, 0, 0);
    // }
    // bool isMatchHelper(const string& s, const string& p, int s_idx, int p_idx){
    //     int s_size = s.size();
    //     int p_size = p.size();
    //     if (p_idx >= p_size && s_idx < s_size){
    //         return false;
    //     }

    //     if (p_idx >= p_size && s_idx >= s_size){
    //         return true;
    //     }
    //     if(isalpha(p[p_idx]) || p[p_idx] == '?'){
    //         if (s_idx >= s_size){
    //             return false;
    //         }
    //         else if (isalpha(p[p_idx])){
    //             return (s[s_idx] == p[p_idx]) && (isMatchHelper(s, p, s_idx + 1, p_idx + 1));
    //         }
    //         else{
    //             return (isalpha(s[s_idx])) && (isMatchHelper(s, p, s_idx + 1, p_idx + 1));
    //         }
    //     }
    //     else{ // this case p[p_idx] == '*'
    //         for( int tmp_idx {s_idx}; tmp_idx <= s_size; ++tmp_idx){
    //            if(isMatchHelper(s, p, tmp_idx, p_idx + 1)){
    //                 return true;
    //            }
    //         }
    //         return false;
    //     }
    }
};
// @lc code=end

