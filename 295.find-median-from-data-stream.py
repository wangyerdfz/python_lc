#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start





class heap: # 1 index
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.heap = [0] * (self.max_size + 1)
        self.front = 1
        # self.heap[0] = -10**6


    def has_left_child(self, pos):
        return pos * 2 <= self.size

    def has_right_child(self, pos):
        return pos * 2 + 1 <= self.size
    
    def left_child_pos(self, pos):
        return pos * 2

    def right_child_pos(self, pos):
        return pos * 2 + 1

    def has_parent(self, pos):
        return pos > 1

    def get_parent(self, pos):
        return pos // 2

    def get_top(self):
        if self.size >= 1:
            return self.heap[self.front]

    def is_leaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def get_size(self):
        return self.size

    

class min_heap(heap):

    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            if self.has_right_child(pos):
                if (self.heap[pos] > self.heap[self.left_child_pos(pos)]) or \
                   (self.heap[pos] > self.heap[self.right_child_pos(pos)]) :
                    if self.heap[self.left_child_pos(pos)] < self.heap[self.right_child_pos(pos)]:
                        self.swap(pos, self.left_child_pos(pos))
                        self.min_heapify(self.left_child_pos(pos))

                    else:
                        self.swap(pos, self.right_child_pos(pos))
                        self.min_heapify(self.right_child_pos(pos))
            else:
                if self.heap[pos] > self.heap[self.left_child_pos(pos)]:
                    self.swap(pos, self.left_child_pos(pos))
    
    def insert(self, element):
        if self.size >= self.max_size:
            return 
        self.size += 1
        self.heap[self.size] = element
        cur_pos = self.size
        while(self.has_parent(cur_pos)):
            if self.heap[cur_pos] < self.heap[self.get_parent(cur_pos)]:
                self.swap(cur_pos, self.get_parent(cur_pos))
                cur_pos = self.get_parent(cur_pos)
            else:
                break

    def min_heap(self):
        for cur_pos in range(self.size // 2, 0, -1):
            self.min_heapify(cur_pos)

    def remove(self):
        popped_val = self.heap[self.front]
        self.swap(self.front, self.size)
        self.size -= 1
        self.min_heapify(self.front)
        return popped_val




class max_heap(heap):

    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            if self.has_right_child(pos):
                if (self.heap[pos] < self.heap[self.left_child_pos(pos)]) or \
                   (self.heap[pos] < self.heap[self.right_child_pos(pos)]):
                    if self.heap[self.left_child_pos(pos)] > self.heap[self.right_child_pos(pos)]:
                        self.swap(pos, self.left_child_pos(pos))
                        self.max_heapify(self.left_child_pos(pos))
                    else:
                        self.swap(pos, self.right_child_pos(pos))
                        self.max_heapify(self.right_child_pos(pos))
            else:
                if self.heap[pos] < self.heap[self.left_child_pos(pos)]:
                    self.swap(pos, self.left_child_pos(pos))   

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        cur_pos = self.size
        while(self.has_parent(cur_pos)):
            if self.heap[cur_pos] > self.heap[self.get_parent(cur_pos)]:
                self.swap(cur_pos, self.get_parent(cur_pos))
                cur_pos = self.get_parent(cur_pos)
            else:
                break

    def max_heap(self):
        for cur_pos in range(self.size // 2, 0, -1):
            self.max_heapify(cur_pos)

    def remove(self):
        popped_val = self.heap[self.front]
        self.swap(self.front, self.size)
        self.size -= 1
        self.max_heapify(self.front)
        return popped_val





class MedianFinder:

    def __init__(self):
        self.min_hp = min_heap(50050)
        self.max_hp = max_heap(50050)
        self.size = 0

    def rebalance(self):
        if self.min_hp.size > self.max_hp.size + 1:
            tmp = self.min_hp.remove()
            self.max_hp.insert(tmp)
        elif self.max_hp.size > self.min_hp.size + 1:
            tmp = self.max_hp.remove()
            self.min_hp.insert(tmp)
        
        

    def addNum(self, num: int) -> None:
        if self.size == 0:
            self.min_hp.insert(num)
        elif self.min_hp.size == 0:
            if self.max_hp.get_top() >= num:
                self.max_hp.insert(num)
            else:
                self.min_hp.insert(num)
        elif self.max_hp.size == 0:
            if self.min_hp.get_top() <= num:
                self.min_hp.insert(num)
            else:
                self.max_hp.insert(num)
        else:
            if self.max_hp.get_top() >= num:
                self.max_hp.insert(num)
            else:
                self.min_hp.insert(num)
        self.size += 1
        self.rebalance()

    def findMedian(self) -> float:
        if self.size == 0:
            return -1
        if self.min_hp.size == self.max_hp.size:
            return (self.min_hp.get_top() + self.max_hp.get_top())/2
        if self.min_hp.size > self.max_hp.size:
            return self.min_hp.get_top()
        return self.max_hp.get_top()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

