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
            print(number,"is enqueued")
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
                print(self.elements[i])
q=Queue(4)
q.enqueue(13983)
q.enqueue(10080)
q.enqueue(7113)
q.enqueue(2520)
for i in range(q.front,q.rear+1):
    flag=0
    for j in range(1,11):
        
        if q.elements[i]%j==0:
            flag+=1
    if flag==10:
        print(q.elements[i])


