






class stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.data = [0] * max_size
        self.front = 0

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size >= self.max_size

    def push(self, val):
        if self.is_full():
            return None
        self.front += 1
        self.front = self.front % self.max_size
        self.data[self.front] =  val
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        popped = self.data[self.front]
        self.front -= 1
        if self.front < 0:
            self.front = self.front + self.max_size
        self.size -= 1
        return popped

    def print(self):
        start = self.front - self.size + 1
        if start >= 0:
            print(self.data[start : (self.front + 1)])
        else:
            start = start + self.max_size
            print(self.data[start:self.max_size] + self.data[0:(self.front + 1)])


if __name__ == '__main__':
    my_stack = stack(20)
    for i in range(10):
        my_stack.push(i)
        my_stack.print()


    for i in range(20, 100):
        my_stack.push(i)
        my_stack.print()
        print(my_stack.pop())
        my_stack.print()

    for i in range(10):
        print(my_stack.pop())
        my_stack.print()
            
