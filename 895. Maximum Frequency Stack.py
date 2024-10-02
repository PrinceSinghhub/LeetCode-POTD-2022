import queue


class FreqStack:

    def __init__(self):
        self.mem = {}
        self.pq = queue.PriorityQueue()
        self.count = 0

    def push(self, x):
        self.count += 1
        self.mem[x] = self.mem.get(x, 0) + 1
        self.pq.put((-self.mem[x], -self.count, x))

    def pop(self) -> int:
        _, _, val = self.pq.get()
        self.mem[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()