class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while  len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.stack1)
print(q.stack2)

print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())

print(q.dequeue())