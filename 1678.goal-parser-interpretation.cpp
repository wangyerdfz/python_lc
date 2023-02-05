/*
 * @lc app=leetcode id=1678 lang=cpp
 *
 * [1678] Goal Parser Interpretation
 */

// @lc code=start
class Solution {
public:
    string interpret(string command) {
        string res = "";
        vector<char> stack;
        for(char c : command){
            if (!stack.empty()){
                if (c == ')'){
                    if (stack.back() == '('){
                        res = res + "o";
                        stack.pop_back();
                    }
                    else{
                        res = res + "al";
                        stack.pop_back();
                        stack.pop_back();
                        stack.pop_back();
                    }
                }
                else{
                    stack.push_back(c);
                }
            }
            else{
                if( c == '('){
                    stack.push_back(c);
                }
                else{
                    res = res + c;
                }
            }
        }
        return res;
    }
};
// @lc code=end

