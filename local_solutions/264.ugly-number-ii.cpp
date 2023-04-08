#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int nthUglyNumber(int n) {
    if (n <= 6){
        return n;
    }
    
    unordered_map<int, int> pos;
    vector<int> ug_num(n + 1, -1);
    for(int i = 1; i <= 6; ++i){
        pos[i] = i;
        ug_num[i] = i;
    }
    int count = 6;
    for (int i = 7; count < n; ++i){
        if (i % 2 == 0){
            if (pos.find(i / 2) != pos.end()){
                count += 1;
                ug_num[count] = i;
                pos[i] = count;
            }
        }
        else if (i % 3 == 0){
            if (pos.find(i / 3) != pos.end()){
                count += 1;
                ug_num[count] = i;
                pos[i] = count;
            }
        }
        else if (i % 5 == 0){
            if (pos.find(i / 5) != pos.end()){
                count += 1;
                ug_num[count] = i;
                pos[i] = count;
            }
        }
    }
    for(int i = 1; i < n; ++i){
        cout << i << " number : " << ug_num[i] << endl;
    }
    return ug_num[n];

}


int main(){
    cout << nthUglyNumber(100) << endl;
    return 1;
}