#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start


class heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.front = 1
        self.heap = [0] * (max_size + 1)

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

    def print(self):
        print(self.heap[1:self.size + 1])

    def is_leaf(self, pos):
        return not self.has_left_child(pos)

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def has_priority(self, fpos, spos):
        if fpos > spos :
            return 1
        if fpos == spos :
            return 0
        return -1

    # def has_priority(self, fpos, spos):
    #     if self.heap[fpos] < self.heap[spos]:
    #         return 1
    #     if self.heap[fpos] == self.heap[spos]:
    #         return 0
    #     return -1

    def heap_up(self, pos):
        while(self.has_parent(pos)):
            if self.has_priority(pos, self.parent(pos)) == 1:
                self.swap(pos, self.parent(pos))
                pos = self.parent(pos)
            else:
                break

    def heapify(self, pos):
        if not self.is_leaf(pos):
            if self.has_right_child(pos):
                if self.has_priority(self.left_child(pos), pos) == 1 or \
                   self.has_priority(self.right_child(pos), pos) == 1:
                    if self.has_priority(self.left_child(pos), self.right_child(pos)) == 1:
                        self.swap(pos, self.left_child(pos))
                        self.heapify(self.left_child(pos))
                    else:
                        self.swap(pos, self.right_child(pos))
                        self.heapify(self.right_child(pos))
            else:
                if self.has_priority(self.left_child(pos), pos) == 1:
                    self.swap(self.left_child(pos), pos)





    def insert(self, element):
        if self.size >= self.max_size:
            return 
        self.size += 1
        self.heap[self.size] = element

        self.heap_up(self.size)

        
    def peek(self):
        if self.size >= 1:
            return self.heap[self.front]

    def remove_val(self, val):
        tmp_pos = self.search(val)
        if tmp_pos == -1:
            return None
        return self.remove(tmp_pos)



    def remove(self, pos = None):
        if pos is None:
            pos = self.front
        if pos > self.size:
            return None
        if self.size <= 0:
            return 
        popped = self.heap[pos]
        self.heap[pos] = self.heap[self.size]
        self.size -= 1
        self.heapify(pos)
        if pos != self.front:
            self.heap_up(pos)
        return popped

    def search(self, val):
        for pos in range(1, self.size + 1):
            if self.heap[pos] == val:
                return pos
        return -1

    def total_heapify(self):
        for pos in range(self.size // 2 , 0, -1):
            self.heapify(pos)



class min_heap(heap):
    def has_priority(self, fpos, spos):
        if self.heap[fpos] < self.heap[spos]:
            return 1
        if self.heap[fpos] == self.heap[spos]:
            return 0
        return -1


class max_heap(heap):
    def has_priority(self, fpos, spos):
        if self.heap[fpos] > self.heap[spos]:
            return 1
        if self.heap[fpos] == self.heap[spos]:
            return 0
        return -1



class deque:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.data = [0] * max_size
        self.left = 0
        self.right = 0

    def peek_left(self):
        if self.is_empty():
            return None
        return self.data[self.left]

    def peek_right(self):
        if self.is_empty():
            return None
        return self.data[self.right]


    def push_left(self, val):
        if self.is_full():
            return 
        if self.is_empty():
            self.data[0] = val
            self.left = 0
            self.right = 0
            self.size += 1
        else:
            self.left -= 1
            if self.left < 0:
                self.left = self.left + self.max_size
            self.data[self.left] = val
            self.size += 1
        

    def push_right(self, val):
        if self.is_full():
            return
        if self.is_empty():
            self.data[0] = val
            self.left = 0
            self.right = 0
            self.size += 1
        else:
            self.right += 1
            self.right = self.right % self.max_size
            self.data[self.right] = val
            self.size += 1

    def pop_left(self):
        if self.is_empty():
            return None

        popped = self.data[self.left]
        self.size -= 1
        self.left += 1
        self.left = self.left % self.max_size
        return popped
    
    def pop_right(self):
        if self.is_empty():
            return None
        
        popped = self.data[self.right]
        self.right -= 1
        if self.right < 0:
            self.right = self.right + self.max_size
        self.size -= 1
        return popped

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.max_size

    def print(self):
        if self.is_empty():
            print('empty\n')
        if self.left <= self.right:
            print(self.data[self.left: (self.right + 1)])
        else:
            print(self.data[self.left: self.max_size] + self.data[0 : self.right + 1])



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 0:
            return []

        ret_list = []
        deq = deque(10010)
        for i, cur in enumerate(nums):
            while (not deq.is_empty()) and nums[deq.peek_right()] <= cur:
                deq.pop_right()
            deq.push_right(i)
            if deq.peek_left() == i - k:
                deq.pop_left()
            if i >= k - 1:
                ret_list.append(nums[deq.peek_left()])

        return ret_list
            




        # max heap method, wont work
        # n = len(nums)
        # if k > n :
        #     return []
        # max_hp = max_heap(100010)
        # for i in range(k):
        #     max_hp.insert(nums[i])
        # ret_list = []
        # ret_list.append(max_hp.peek())
        # end_idx = k
        # start_idx = 0
        # while(end_idx < n):
        #     if nums[start_idx] == max_hp.peek():
        #         max_hp.remove()
        #     max_hp.insert(nums[end_idx])
        #     ret_list.append(max_hp.peek())
        #     start_idx += 1 
        #     end_idx += 1
        # return ret_list

# @lc code=end

