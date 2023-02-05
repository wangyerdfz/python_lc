/*
 * @lc app=leetcode id=874 lang=cpp
 *
 * [874] Walking Robot Simulation
 */

// @lc code=start
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        // facing : 0 north, 1 east, 2 south, 3 west
        int cur_x = 0;
        int cur_y = 0;
        int facing = 0; // north
        int max_dis = 0;
        for (int a : commands){
            if ( a == -2){
                facing = (facing + 3)%4;
                continue;
            }
            if ( a == -1){
                facing = ( facing + 1) % 4;
                continue;
            }
            else{
                int target_x = cur_x;
                int target_y = cur_y;
                bool hit = false;
                for(int i = 0; i < a; ++i){
                    if ( facing == 0){
                        target_x = cur_x ;
                        target_y = cur_y + 1;
                    }
                    if (facing == 1){
                        target_x = cur_x + 1;
                        target_y = cur_y;
                    }
                    if (facing == 2){
                        target_x = cur_x;
                        target_y = cur_y - 1;
                    }
                    if (facing == 3){
                        target_x = cur_x - 1;
                        target_y = cur_y;
                    }
                    for (auto ob : obstacles){
                        if (target_x == ob[0] && target_y == ob[1]){
                            hit = true;
                            break;
                        }
                    }
                    if (hit){
                        break;
                    }
                    cur_x = target_x;
                    cur_y = target_y;
                }
                if (cur_x * cur_x + cur_y * cur_y > max_dis){
                        max_dis = cur_x * cur_x + cur_y * cur_y;
                } 
            }
        }
        return max_dis;
    }
};
// @lc code=end

