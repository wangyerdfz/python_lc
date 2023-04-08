
import sys

class min_heap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = -1 * sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos // 2

    def has_parent(self, pos):
        return (pos//2 >= 1)

    def has_left_child(self, pos):
        return self.left_child(pos) <= self.size
    
    def has_right_child(self, pos):
        return self.right_child(pos) <= self.size


    def left_child(self, pos):
        return pos * 2

    def right_child(self, pos):
        return pos * 2 + 1

    def is_leaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            if (self.heap[pos] > self.heap[self.left_child(pos)]) or \
                (self.heap[pos] > self.heap[self.right_child(pos)]):
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))

                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element
        # print(self.heap)
        current_idx = self.size
        while(self.has_parent(current_idx)):
            if self.heap[current_idx] < self.heap[self.parent(current_idx)]:
                self.swap(current_idx, self.parent(current_idx))
                current_idx = self.parent(current_idx)
            else:
                break
        print(self.heap)

    def print(self):
        if self.size <= 1:
            print(f'The heap only has {self.size} elements, no print')
        for i in range(1, (self.size // 2) + 1):
            first_str = f'Parent :  {self.heap[i]}, '
            if self.has_left_child(i):
                second_str = f'Left Child : {self.heap[self.left_child(i)]}, '
            else:
                second_str = f'No Left Child, '
            if self.has_right_child(i):
                third_str = f'Right Child : {self.heap[self.right_child(i)]}, '
            else:
                third_str = f'No Right Child, '

            print(first_str + second_str + third_str)
        print('End of print')

    def min_heap(self):
        for pos in range(self.size//2, 0, -1):
            self.min_heapify(pos)

    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.min_heapify(self.front)
        return popped

    
if __name__ == '__main__':
    print(f'The min heap is :')
    min_hp = min_heap(15)
    min_hp.insert(5)
    min_hp.print()
    min_hp.insert(3)
    min_hp.print()
    min_hp.insert(17)
    min_hp.insert(10)
    min_hp.insert(84)
    min_hp.insert(19)
    min_hp.insert(6)
    min_hp.insert(22)
    min_hp.insert(9)
    min_hp.print()
    min_hp.min_heap()
  
    min_hp.print()
    print("The Min val is " + str(min_hp.remove()))
    min_hp.print()



     
