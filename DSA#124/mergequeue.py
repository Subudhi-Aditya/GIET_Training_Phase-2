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
            # print(val,"is dequeued")
            return val
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.elements[i])
    def maxsize(self):
        return self.max_size
q1=Queue(2)
q2=Queue(3)
q3=Queue(q1.maxsize()+q2.maxsize())
q1.enqueue(10)
q1.enqueue(11)
q2.enqueue(12)
q2.enqueue(13)
q2.enqueue(14)
# print("hi")
while(q1.rear>=q1.front and q2.front<=q2.rear):
    q3.enqueue(q1.elements[q1.front])
    q3.enqueue(q2.elements[q2.front])
    q1.front+=1
    q2.front+=1
    # print(q1.front)
    # print(q2.front)
if q1.isempty():
    if not q2.isempty():
        while(q2.front<=q2.rear):
            q3.enqueue(q2.elements[q2.front])
            q2.front+=1
else:
    if not q1.isempty():
        while(q1.front<=q1.rear):
            q3.enqueue(q1.elements[q1.front])
            q1.front+=1
q3.display()
