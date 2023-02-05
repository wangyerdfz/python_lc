#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start

class min_heap:
    def __init__(self, x, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * (max_size + 1)
        self.front = 1
        self.x = x

    def compare(self, pos1, pos2): # -1 : left < right 0 : left == right, 1 left > right
        if abs(self.heap[pos1] - self.x) < abs(self.heap[pos2] - self.x):
            return -1
        if abs(self.heap[pos1] - self.x) == abs(self.heap[pos2] - self.x):
            if self.heap[pos1] < self.heap[pos2]:
                return -1
            if self.heap[pos1] == self.heap[pos2]:
                return 0
            if self.heap[pos1] > self.heap[pos2]:
                return 1
        return 1

    def parent(self, pos):
        return pos // 2
    
    def has_parent(self, pos):
        return pos > 1

    def has_left_child(self, pos):
        return pos * 2 <= self.size

    def has_right_child(self, pos):
        return pos * 2 + 1 <= self.size

    def left_child(self, pos):
        return pos * 2

    def right_child(self, pos):
        return pos * 2 + 1

    def is_leaf(self, pos):
        return not self.has_left_child(pos)

    def peek(self):
        return self.heap[self.front]

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            if self.has_right_child(pos):
                if self.compare(pos, self.left_child(pos)) == -1 or \
                   self.compare(pos, self.right_child(pos)) == -1 :
                    if self.compare(self.left_child(pos), self.right_child(pos)) == 1 :
                        self.swap(self.left_child(pos), pos)
                        self.min_heapify(self.left_child(pos))
                    else:
                        self.swap(self.right_child(pos), pos)
                        self.min_heapify(self.right_child(pos))
            else:
                if self.compare(pos, self.left_child(pos)) == -1:
                    self.swap(pos, self.left_child(pos))
        
    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        cur_idx = self.size
        while(self.has_parent(cur_idx)):
            if self.compare(cur_idx, self.parent(cur_idx)) == 1:
                self.swap(cur_idx, self.parent(cur_idx))
                cur_idx = self.parent(cur_idx)
            else:
                break

    def min_heap(self):
        for i in range(self.size//2, 0, - 1):
            self.min_heapify(i)
        
    def remove(self):
        if self.size >= 1:
            popped = self.heap[self.front]
            self.swap(self.front, self.size)
            self.size -= 1
            self.min_heapify(self.front)
            return popped
        return None
    
    def print(self):
        print(self.heap[self.front:(self.size + 1)])

def compare_two_nums(num1, num2, x):
    if abs(num1 - x) < abs(num2 - x):
            return -1
    if abs(num1 - x) == abs(num2 - x):
        if num1 < num2:
            return -1
        if num1 == num2:
            return 0
        if num1 > num2:
            return 1
    return 1

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n < k:
            return -1
        min_hp = min_heap(x, 10000)
        for i in range(k):
            min_hp.insert(arr[i])
        for i in range(k, n):
            top = min_hp.peek()
            if compare_two_nums(arr[i], top, x) in [0, -1]:
                min_hp.insert(arr[i])
                min_hp.remove()
        new_list = min_hp.heap[1:(k + 1)]
        new_list.sort()
        return new_list
# @lc code=end

