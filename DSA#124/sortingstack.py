class Stack:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.tp=-1
    def isempty(self):
        if self.tp==-1:
            return True
        return False
    def isfull(self):
        if self.tp==self.max_size-1:
            return True
        return False
    def push(self,number):
        if self.isfull():
            print("The stack is full",number,"cannot be pushed")
        else:
            self.tp+=1
            self.elements[self.tp]=number
            # print(number,"is pushed")
    def pop(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            val=self.elements[self.top]
            self.tp-=1
            
            # print(val,"is poped")
            return val
    def display(self):
        for i in range(self.tp,-1,-1):
            print(self.elements[i],end=" ")
        print()
    def top(self):
        return self.elements[self.tp]
        
a=Stack(6)
a.push(5)
a.push(88)
a.push(6)
a.push(4)
a.push(7)
a.push(89)
b=Stack(6)
c=Stack(6)
a.display()
# mini=-100
l=[]
# # a.top-=1
# # print(a.top())
# # print(l)
# # min=a.tp
while a.tp>=0:
    l.append(a.top())
    a.tp-=1
# print(l)
min=min(l)
# print(min)
freq=0
for i in l:
    if i==min:
        freq+=1
# print(freq)
for i in range(0, len(l)):
    if l[i]!=min:
        b.push(l[i])


# b.display()


# c.display()

for i in range(0,freq):
    c.push(min)
top1=b.tp
while b.tp>=0:
    c.push(b.top())
    b.tp-=1
c.display()
# a.display()