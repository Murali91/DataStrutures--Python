class Queue:
    def __init__(self):
        self.queue = list()
    def enqueue(self,item):
        self.queue.insert(0,item)
    def dequeue(self):
        return "Deleted Item: "+str(self.queue.pop())
    def peek(self):
        return self.queue[len(self.queue)-1]
    def isEmpty(self):
        return len(self.queue)==0
    def display(self):
        return self.queue
