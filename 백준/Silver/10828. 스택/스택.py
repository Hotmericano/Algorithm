import sys
input = sys.stdin.readline

class ArrayStack():
    def __init__(self, size):
        self.size = size
        self.top = 0
        self.bottom = 0
        self.array = [None]*size

    def isEmpty(self):
        return self.top == self.bottom
    
    def isFull(self):
        return self.top == self.size
    
    def push(self, e):
        if self.isFull() is not True:
            self.array[self.top] = e
            self.top += 1
        else:
            pass

    def pop(self):
        if self.isEmpty() is not True:
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
            return self.array[self.top-1]
    
n = int(input())
stack = ArrayStack(n)

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif 'pop' == command[0]:
        print(stack.pop())
    elif 'size' == command[0]:
        print(stack.returnSize())
    elif 'top' == command[0]:
        print(stack.returnTop())
    elif 'empty' == command[0]:
        state = stack.isEmpty()
        if state:
            print(1)
        else:
            print(0)


