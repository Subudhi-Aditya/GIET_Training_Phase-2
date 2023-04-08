class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def isempty(self):
        if self.__front>self.__rear:
            return True
        return False
    def isfull(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def enqueue(self,number):
        if self.isfull():
            print("Queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=number
            print(number,"is enqueued")
    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            val=self.__elements[self.__front]
            self.__front+=1
            print(val,"is dequeued")
            return val
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            for i in range(self.__front,self.__rear+1):
                print(self.__elements[i])
q=Queue(3)
q.enqueue(10)
q.enqueue(12)
q.enqueue(14)
q.enqueue(19)
q.display()
q.dequeue()
q.display()

