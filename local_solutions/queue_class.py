


class queue:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.data = [0] * max_size
        self.front = 0
        

    def is_full(self):
        return self.size >= self.max_size
    
    def is_empty(self):
        return self.size == 0

    def push(self, val):
        if self.is_full():
            return 
        end = (self.size + self.front) % self.max_size
        self.data[end] = val
        self.size += 1
        

    def pop(self):
        if self.is_empty():
            return None
        popped = self.data[self.front]
        self.front += 1
        self.front = self.front % self.max_size
        self.size -= 1
        return popped

    def print(self):
        end = self.front + self.size
        if end <= self.max_size:
            print(self.data[self.front : end])
        else:
            print(self.data[self.front : self.max_size] + self.data[0:(end % self.max_size)])




if __name__ == '__main__':
    my_q = queue(20)
    for i in range(10):
        my_q.push(i)
        my_q.print()
    print(f'Start popping')
    for i in range(20, 100):
        my_q.push(i)
        my_q.print()
        print(my_q.pop())
        my_q.print()