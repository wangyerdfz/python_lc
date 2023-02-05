/*
 * @lc app=leetcode id=155 lang=cpp
 *
 * [155] Min Stack
 */

// @lc code=start

const int max_size = 40000;

class MinStack {
private:
    int size;
    int data[max_size];
    int min[max_size];
public:
    MinStack() {
        size = 0;
    }
    
    void push(int val) {
        if (size == 0){
            data[size] = val;
            min[size] = val;
            size++;
            return;
        }
        if (size > max_size){
            return;
        }
        data[size] = val;
        if(min[size - 1] > val){
            min[size] = val;
        }
        else{
            min[size] = min[size - 1];
        }
        size++;
        return;
    }
    
    void pop() {
        if (size <= 0){
            return;
        }
        size--;
        return;
    }
    
    int top() {
        if (size <= 0){
            return INT_MAX;
        }
        return data[size - 1];
    }
    
    int getMin() {
        if (size <= 0){
            return INT_MAX;
        }
        return min[size - 1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
// @lc code=end

