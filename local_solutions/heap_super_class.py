



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

class median_finder():
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.min_hp = min_heap(max_size)
        self.max_hp = max_heap(max_size)

    def add(self, element):
        if self.size == 0:
            self.min_hp.insert(element)

        elif self.min_hp.size > 0:
            if element > self.min_hp.peek():
                self.min_hp.insert(element)

            else:
                self.max_hp.insert(element)

        else:
            if element < self.max_hp.peek():
                self.max_hp.insert(element)

            else:
                self.min_hp.insert(element)

        self.size += 1
        self.rebalance()

    def rebalance(self):
        if self.min_hp.size > self.max_hp.size + 1:
            tmp = self.min_hp.remove()
            # print(f'swap  {tmp}')
            self.max_hp.insert(tmp)

        elif self.min_hp.size + 1 < self.max_hp.size:
            tmp = self.max_hp.remove()
            self.min_hp.insert(tmp)

    def get_median(self):
        if self.size <= 0:
            return 
        if self.min_hp.size > self.max_hp.size:
            return self.min_hp.peek()
        elif self.min_hp.size < self.max_hp.size:
            return self.max_hp.peek()
        else:
            return (self.min_hp.peek() + self.max_hp.peek())/2

    def print(self):
        self.min_hp.print()
        self.max_hp.print()


if __name__ == '__main__':
    # mf = median_finder(1000)
    # for i in range(100):
    #     mf.add(i)
    #     # mf.print()
    #     print(mf.get_median())

    

    # min_hp = min_heap(10000)
    # min_hp.insert(0)
    # min_hp.print()
    # min_hp.insert(1)
    # min_hp.print()
    # min_hp.remove()
    # min_hp.print()
    min_hp = min_heap(1000)  
    for i in range(10):
        min_hp.insert(i)
        min_hp.print()

    for i in range(9):
        print(min_hp.remove_val(i))
        min_hp.print()

    


