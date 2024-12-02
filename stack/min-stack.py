class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.stack_min.append(val)
        else:
            self.stack.append(val)
            self.stack_min.append(min(self.stack_min[-1], val))

        

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()