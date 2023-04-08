class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def isempty(self):
        if self.__top==-1:
            return True
        return False
    def isfull(self):
        if self.__top==self.__max_size-1:
            return True
        return False
    def push(self,number):
        if self.isfull():
            print("The stack is full",number,"cannot be pushed")
        else:
            self.__top+=1
            self.__elements[self.__top]=number
            # print(number,"is pushed")
    def pop(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            val=self.__elements[self.__top]
            self.__top-=1
            
            print(val,"is poped")
            return val
    def display(self):
        for i in range(self.__top,-1,-1):
            print(self.__elements[i],end=" ")
        print()
    def top(self):
        return self.__elements[self.__top]


class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.rear=-1
        self.front=0
    def isempty(self):
        if self.front>self.rear:
            return True
        return False
    def isfull(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def enqueue(self,number):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear+=1
            self.elements[self.rear]=number
            # print(number,"is enqueued")
    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            val=self.elements[self.front]
            self.front+=1
            print(val,"is dequeued")
            return val
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.elements[i],end=" ")
        print()

def traingle(a,b):
    sum1=0
    for i in range(1,a+1):
        sum1+=i
    if sum1==b:
        return True
    return False
q=Queue(10)
q.enqueue(7)
q.enqueue(28)
q.enqueue(8)
q.enqueue(35)
q.enqueue(3)
q.enqueue(6)
q.enqueue(5)
q.enqueue(15)
q.enqueue(2)
q.enqueue(5)
q.display()
s=Stack(10)
for i in range(q.front,q.rear):
    if traingle(q.elements[i],q.elements[i+1]):
        s.push(q.elements[i+1])
s.display()


