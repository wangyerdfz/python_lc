#include <iostream>
#include <cmath>
using std::pow;
using std::cout;
using std::endl;
const int MAX_VARIATION = 1048577;
const int MAX_TOTAL = 21;



bool is_number_in(unsigned rep, int number){
    return bool( (rep >>(number - 1)) & 1);
}
unsigned mark_number_as_unavailable(unsigned rep, int number){
    return rep & (~(1U << (number - 1)));
}
int count_rep_sum(unsigned rep){
    int cur_num= 1;
    int sum_ = 0;
    while(rep > 0){
        sum_ += (rep & 1) * cur_num;
        rep = rep >> 1;
        cur_num++;
    }
    return sum_;
}

bool canIWin(int maxChoosableInteger, int desiredTotal) {
    if (desiredTotal == 0){
        return true;
    }
    if(count_rep_sum(pow(2, maxChoosableInteger) - 1) < desiredTotal){
        return false;
    }
    int rep_total = pow(2, maxChoosableInteger);
    // we need two dimensional array, 2**maxChooseableInteger + 1 by desiredTotal + 1
    bool res[2049][21] = {false};
    for(unsigned rep = 0; rep <= pow(2, maxChoosableInteger); rep++){
        res[rep][0] = true;
    }
    for(int total = 1; total <= desiredTotal; total++){
        for(unsigned rep = 0; rep <= rep_total; rep++){
            cout << total << rep << endl;
            if (count_rep_sum(rep) < total){
                res[rep][total] = false;
            }
            for(int number = maxChoosableInteger; number >= 1; number--){
                if (is_number_in(rep, number)){
                    if(number >= total){
                        res[rep][total] = true;
                        break;
                    }
                    else if(!res[mark_number_as_unavailable(rep, number)][total - number]){
                        res[rep][total] = true;
                        break;
                    }
                }
            }
        }
    }
    return res[rep_total - 1][desiredTotal];

}

int main(){
    cout << "hello" << endl;
    bool res = canIWin(10, 1);
    cout << res << endl;
    return 0;
}