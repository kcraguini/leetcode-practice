from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.length = 0
        self.sum = 0
        self.max = size
        
    def next(self, val: int) -> float:
        if self.length < self.max:
            self.sum += val
            self.queue.append(val)
            self.length += 1
        else:
            self.sum -= self.queue.popleft()
            self.sum += val
            self.queue.append(val)
        return self.sum / self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

movingAvg = MovingAverage(3)
print(movingAvg.next(1)) # return 1.00000 = 1 / 1
print(movingAvg.next(10)) # return 5.50000 = (1 + 10) / 2
print(movingAvg.next(3)) # return4.66667 = (1 + 10 + 3) / 3
print(movingAvg.next(5)) # return 6.00000 = (10 + 3 + 5) / 3