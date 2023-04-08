class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.queue=[None]*self.max_size
        self.front=0
        self.rear=-1
    def isempty(self):
        if self.front>self.rear:
            return True
        return False
    def isfull(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def enqueue(self,data):
        self.rear+=1
        self.queue[self.rear]=data
    def dequeue(self):
        if self.isempty():
            print("The stack is empty")
        else:
            self.front+=1
    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=" ")
        print()
q=Queue(7)
q.enqueue(2)
q.enqueue(7)
q.enqueue(9)
q.enqueue(4)
q.enqueue(6)
q.enqueue(5)
q.enqueue(10)
a=Queue(7)
b=Queue(7)
# q.display()
for i in range(q.front,q.rear+1):
    if q.queue[i]%2==0:
        a.enqueue(q.queue[i])
print("The even queue")
a.display()
for i in range(q.front,q.rear+1):
    if q.queue[i]%2!=0:
        b.enqueue(q.queue[i])
print("the odd queue")
b.display()



