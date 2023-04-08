#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
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


class max_heap:
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

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            if self.has_right_child(pos):
                if self.heap[pos] < self.heap[self.left_child(pos)] or \
                   self.heap[pos] < self.heap[self.right_child(pos)] :
                    if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)] :
                        self.swap(self.left_child(pos), pos)
                        self.max_heapify(self.left_child(pos))
                    else:
                        self.swap(self.right_child(pos), pos)
                        self.max_heapify(self.right_child(pos))
            else:
                if self.heap[pos] < self.heap[self.left_child(pos)]:
                    self.swap(pos, self.left_child(pos))
        
    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        cur_idx = self.size
        while(self.has_parent(cur_idx)):
            if self.heap[cur_idx] > self.heap[self.parent(cur_idx)]:
                self.swap(cur_idx, self.parent(cur_idx))
                cur_idx = self.parent(cur_idx)
            else:
                break

    def max_heap(self):
        for i in range(self.size//2, 0, - 1):
            self.max_heapify(i)
        
    def remove(self):
        if self.size >= 1:
            popped = self.heap[self.front]
            self.swap(self.front, self.size)
            self.size -= 1
            self.max_heapify(self.front)
            return popped
        return None



class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.min_hp = min_heap(20000)
        for i in nums:
            self.min_hp.insert(i)

        while(self.min_hp.size > k):
            self.min_hp.remove()
        self.min_hp.print()

    def add(self, val: int) -> int:
        if val <= self.min_hp.peek():
            self.min_hp.print()
            return self.min_hp.peek()

        self.min_hp.insert(val)
        self.min_hp.remove()
        self.min_hp.peek()
        self.min_hp.print()

if __name__ == '__main__':
    kth = KthLargest(3, [4,5,8,2])
    print(kth.add(3))
    kth.add(5)
    kth.add(10)
    kth.add(9)
    kth.add(4)





# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

