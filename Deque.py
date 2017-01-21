class Deque:
    def __init__(self):
        self.queue = []
    def addFront(self,item):
        self.queue.insert(0,item)
    def addRear(self,item):
        self.queue.append(item)
    def rmvFront(self):
        self.queue.pop(0)
    def rmvRear(self):
        self.queue.pop()
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return len(self.queue)==0
    def display(self):
        return self.queue
