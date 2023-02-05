/*
 * @lc app=leetcode id=1394 lang=cpp
 *
 * [1394] Find Lucky Integer in an Array
 */

// @lc code=start
class Solution {
public:
    int findLucky(vector<int>& arr) {
        int n = arr.size();
        if (n <= 0){
            return -1;
        }
        unordered_map<int, int> freq;
        for(int i: arr){
            if(freq.find(i) == freq.end()){
                freq[i] = 1;
            }
            else{
                freq[i] += 1;
            }
        }
        int largest = -1;
        for(auto i : freq){
            if (i.first == i.second){
                if (i.first > largest){
                    largest = i.first;
                }
            }
        }
        return largest;
    }
};
// @lc code=end

