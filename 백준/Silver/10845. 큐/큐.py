import sys
input = sys.stdin.readline

class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None]*capacity
        self.front = 0
        self.rear = 0
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear + 1)%self.capacity
    def enqueue(self, A):
        if not self.isFull():
            self.rear  = (self.rear + 1)%self.capacity
            self.array[self.rear] = A
        else:
            pass
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1)%self.capacity
            return self.array[self.front]
        else:
            return -1
    def size(self):
        return (self.rear - self.front + self.capacity)%self.capacity
    def display(self, msg = 'queue'):
        print(f"rear: {self.rear}, front: {self.front}")
        print(f"{msg} = [ ",end = '')
        for i in range(self.front + 1, self.front+1+self.size()):
            print(self.array[i%self.capacity], end=' ')
        print(']')
    #포화상태와 관계없이 값을 삽인한 후 만약 포화상태였다면 전단회준 진행해서 가장 오래된 값을 삭제 --> 링 버퍼(ring buffer)
    def enqueue2(self, A):
        self.rear = (self.rear + 1)%self.capacity
        self.array[self.rear] = A
        if (self.isEmpty()):
            self.front = (self.front + 1)%self.capacity
    
    def returnFront(self):
        if self.isEmpty() == False:
            return self.array[self.front+1]
        else:
            return -1
        
    def returnBack(self):
        if self.isEmpty() == False:
            return self.array[self.rear]
        else:
            return -1
    
n = int(input())
queue = ArrayQueue(n)

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.enqueue(int(command[1]))
    elif 'pop' == command[0]:
        print(queue.dequeue())
    elif 'size' == command[0]:
        print(queue.size())
    elif 'front' == command[0]:
        print(queue.returnFront())
    elif 'back' == command[0]:
        print(queue.returnBack())
    elif 'empty' == command[0]:
        state = queue.isEmpty()
        if state:
            print(1)
        else:
            print(0)


