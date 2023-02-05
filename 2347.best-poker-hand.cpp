/*
 * @lc app=leetcode id=2347 lang=cpp
 *
 * [2347] Best Poker Hand
 */

// @lc code=start
class Solution {
    bool if_flush(vector<int> ranks, vector<char>& suits){
        return (suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4]);
    }

public:
    string bestHand(vector<int>& ranks, vector<char>& suits) {
        if(if_flush(ranks, suits)){
            return "Flush";
        }
        unordered_map<int, int> count;
        for(int c: ranks){
            if(count.find(c) == count.end()){
                count[c] = 1;
            }
            else{
                count[c]++;
            }
        }
        int max_count = 0;
        for(auto i : count){
            max_count = max(max_count, i.second);
        }
        if (max_count >= 3){
            return "Three of a Kind";
        }
        if(max_count == 2){
            return "Pair";
        }
        else{
            return "High Card";
        }
    }
};
// @lc code=end

