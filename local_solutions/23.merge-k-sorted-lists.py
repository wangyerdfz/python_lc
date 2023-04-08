#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.front = 1
        self.heap = [0] * (max_size + 1)

    def is_empty(self):
        return self.size == 0

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

class min_pos_heap(heap):
    def has_priority(self, fpos, spos):
        if self.heap[fpos][0] < self.heap[spos][0] :
            return 1
        if self.heap[fpos][0] == self.heap[spos][0] :
            return 0
        return -1

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next



def mergeKLists(lists):
    head = node = ListNode(0)
    min_hp = min_pos_heap(600000)
    for l in lists:
        if l is not None:
            min_hp.insert((l.val, l))
            min_hp.print()
    while not min_hp.is_empty():
        tmp_val, tmp_node = min_hp.remove()
        node.next = ListNode(tmp_val)
        node = node.next
        if tmp_node.next is not None:
            min_hp.insert((tmp_node.next.val, tmp_node.next))
    return head.next

if __name__ == '__main__':
    list_1_head = list_1_iter = ListNode(1)
    list_1_iter.next = ListNode(4)
    list_1_iter = list_1_iter.next
    list_1_iter.next = ListNode(5)


    list_2_head = list_2_iter = ListNode(1)
    list_2_iter.next = ListNode(3)
    list_2_iter = list_2_iter.next
    list_2_iter.next = ListNode(4)


    list_3_head = list_3_iter = ListNode(2)
    list_3_iter.next = ListNode(6)
    
    list_in = [list_1_head, list_2_head, list_3_head]

    mergeKLists(list_in)



# @lc code=end

