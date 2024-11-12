import sys
input = sys.stdin.read

class ArrayStack():
    def __init__(self, size):
        self.size = size
        self.top = 0
        self.bottom = 0
        self.array = [None] * size

    def isEmpty(self):
        return self.top == self.bottom
    
    def isFull(self):
        return self.top == self.size
    
    def push(self, e):
        if not self.isFull():
            self.array[self.top] = e
            self.top += 1
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top]
        else:
            return -1
    
    def returnSize(self):
        return self.top 
    
    def returnTop(self):
        if self.isEmpty():
            return -1
        else:
            return self.array[self.top - 1]

# 전체 입력을 한 번에 읽어온 뒤, 각 줄을 처리
data = input().splitlines()
n = int(data[0])
stack = ArrayStack(n)

for command in data[1:]:
    if command.startswith('push'):
        _, num = command.split()
        stack.push(int(num))
    elif command == 'pop':
        print(stack.pop())
    elif command == 'size':
        print(stack.returnSize())
    elif command == 'top':
        print(stack.returnTop())
    elif command == 'empty':
        print(1 if stack.isEmpty() else 0)
