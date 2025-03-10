'''
ALGORITHM 1 BY: Christopher Alpuerto
'''

# extend build in priority queue to support:
# priority queue mode, stack mode, queue mode

# PRIORITY QUEUE:
'''
elements are dequeued based on their priority
minheap, where the smallest element dequeued first
max-heap, where the largest element dequeued first

'''
# STACK:
'''
queue should behave as LIFO.
Most recently inserted element should be dequeued first
'''
# QUEUE:
'''
queue should behave as FIFO
oldest inserted element should be dequeued first
'''
import heapq
from collections import deque

class CustomQueue():
    def __init__(self, mode: str):
        models = {"priority", "stack", "queue"}
        if mode not in models:
            raise ValueError(f"Mode must be: {models}")
        
        self.mode = mode
        if self.mode == "priority" or self.mode == "stack":
            self.queue = []
        elif self.mode == "queue":
            self.queue = deque()
    def push(self, value, priority=None):
        if self.mode == "priority":
            heapq.heappush(self.queue, (priority if priority is None else value, value))
        elif self.mode == "stack" or self.mode == "queue":
            self.queue.append(value)
    def pop(self):
        if self.is_empty():
            return None
        if self.mode == "priority":
            return heapq.heappop(self.queue)[1]
        return (self.queue.pop() if self.mode =="stack" else self.queue.popleft())
    def is_empty(self):
        return (len(self.queue) == 0)
    
if __name__ == "__main__":
    print("Let's test CustomeQueue priority mode.")
    q = CustomQueue("priority")
    q.push(1, 1)
    q.push(2, 2)
    q.push(3, 3)
    print("Priority Queue: ", q.pop())
    
    print("Now let's test CustomQueue with stack mode. ")
    q = CustomQueue("stack")
    q.push(1)
    q.push(5)
    q.push(10)
    print("Stack: ", q.pop())
    
    print("Finally, lets test CustomQueue with queue mode.")
    q = CustomQueue("queue")
    q.push(3)
    q.push(9)
    q.push(12)
    print("Queue: ", q.pop())

    print("All tests passed!")
