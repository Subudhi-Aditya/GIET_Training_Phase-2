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
                print(self.elements[i])
class person:
    def __init__(self,pname,age,gender):
        self.pname=pname
        self.age=age
        self.gender=gender
    def return_details(self):
        print(self.pname,self.age,self.gender)
    def gender1(self):
        return self.gender
p=person("adi",20,"male")
p1=person("raki",20,"female")
p2=person("sumu",20,"male")
p3=person("sudhi",20,"female")
p4=person("sri",20,"male")
q=Queue(5)
q.enqueue(p)
q.enqueue(p1)
q.enqueue(p2)
q.enqueue(p3)
q.enqueue(p4)
a=input()
for i in range(q.front,q.rear+1):
    if q.elements[i].gender==a:
        print(q.elements[i].pname," ",q.elements[i].age," ",q.elements[i].gender)
        # print(q.elements[i].return_details())
# print(q.elements[q.front].gender1())





