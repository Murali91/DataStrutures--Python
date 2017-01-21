class Stack:
    def __init__(self):
        self.stack = list()
    def display(self):
        print self.stack
    def pop(self):
        return "Deleted Item: "+str(self.stack.pop())
    def push(self,value):
        self.stack.append(value)
    def peek(self):
        return self.stack[len(self.stack)-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
