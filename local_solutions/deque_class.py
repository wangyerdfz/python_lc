
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




if __name__ == '__main__':
    deq = deque(20)

    for i in range(8):
        deq.push_left(i * 2)
        # print(deq.size, deq.data, deq.left, deq.right)
        deq.print()
        deq.push_right(i * 2 + 1)
        # print(deq.size, deq.data, deq.left, deq.right)
        deq.print()

    for i in range(5):
        print(deq.pop_left())
        print(deq.pop_right())
        deq.print()