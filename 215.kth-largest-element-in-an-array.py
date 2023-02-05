#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start


class min_heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * (max_size + 1)
        self.front = 1
        
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
                if self.heap[pos] > self.heap[self.left_child(pos)] or \
                   self.heap[pos] > self.heap[self.right_child(pos)] :
                    if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)] :
                        self.swap(self.left_child(pos), pos)
                        self.min_heapify(self.left_child(pos))
                    else:
                        self.swap(self.right_child(pos), pos)
                        self.min_heapify(self.right_child(pos))
            else:
                if self.heap[pos] > self.heap[self.left_child(pos)]:
                    self.swap(pos, self.left_child(pos))
        
    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        cur_idx = self.size
        while(self.has_parent(cur_idx)):
            if self.heap[cur_idx] < self.heap[self.parent(cur_idx)]:
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

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return -1
        min_hp = min_heap(200001)
        for i in range(k):
            min_hp.insert(nums[i])
        for i in range(k, n):
            if nums[i] < min_hp.peek():
                continue
            else:
                min_hp.insert(nums[i])
                min_hp.remove()
        return min_hp.peek()
# @lc code=end

