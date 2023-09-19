class MinStack:

    def __init__(self):
        self.elems = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.elems:
            self.elems.append(val)
            self.mins.append(val)
            return
        self.elems.append(val)
        min_app = min(self.mins[-1], val)
        self.mins.append(min_app)

    def pop(self) -> None:
        self.elems.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.elems[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()