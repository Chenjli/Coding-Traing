class Stack():
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def top(self):
        return self.stack[-1]
    def pop(self):
        res = self.top()
        self.stack = self.stack[:-1]
        return res
    def isEmpty(self):
        return len(self.stack) == 0
