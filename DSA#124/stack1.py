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
            print(number,"is pushed")
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
            print(self.__elements[i])
    def top(self):
        return self.__elements[self.__top]
        
a=Stack(3)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.display()
a.pop()
a.display()
print(a.top(),"is top element")

