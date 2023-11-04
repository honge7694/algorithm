# 1. 스택은 아래에서 위로 쌓이지만, 
# 2. 스택을 이용하여 큐를 구현할 땐 위에서 아래로 쌓는 식으로 코드작성.

from collections import deque
"""
class MyQueue:
    def __init__(self):
        self.stack = deque()
    def push(self, x):
        self.stack.appendleft(x)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def empty(self):
        return len(self.stack) == 0
"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class MyQueue:
    def __init__(self):
        self.top = None

    def __str__(self):
        result = []
        node = self.top
        while node:
            result.append(node.data)
            node = node.next
        
        return " ".join(map(str, result))

    def push(self, data):
        if not self.top:
            self.top = Node(data, None)
            return
        
        node = self.top
        while node.next: # 스택의 최하단까지 이동
            node = node.next
            
        node.next = Node(data, None)

    def pop(self):
        if not self.top:
            return
        
        node = self.top
        self.top = node.next

        return node.data

    def peek(self):
        node = self.top
        return node.data
    
    def empty(self):
        return self.top is None
    

myQueue = MyQueue()
myQueue.push(1)
print(myQueue)
myQueue.push(2)
print("myQueue 2번째 push : ", myQueue)
myQueue.peek()
myQueue.pop()

print(myQueue)
print(myQueue.empty())