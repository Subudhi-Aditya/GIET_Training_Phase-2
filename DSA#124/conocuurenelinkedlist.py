class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def atbegin(self,data):
        if data=="*" or data=="/":
            data=" "
        newnode=Node(data)
        
        newnode.ref=self.head
        self.head=newnode
    def atend(self,data):
        newnode=Node(data)

        if self.head==None:
            self.atbegin(data)
        else:
            val=self.head
            while(val.ref is not None):
                val=val.ref
            val.ref=newnode
    def list(self):
        val=self.head
        while(val is not None):
            print(val.data,end=" ")
            val=val.ref
        # print("12345")
        # print(val.data)
list=linkedlist()
list.atend('A')
list.atend('n')
list.atend('*')
list.atend('/')
list.atend('a')
list.atend('p')
list.atend('p')
list.atend('l')
list.atend('e')
list.atend('*')
list.atend('a')
list.atend('/')
list.atend('day')
list.atend('*')
list.atend('/')
list.atend('k')
list.atend('e')
list.atend('e')
list.atend('p')
list.atend('s')
list.atend('/')
list.atend('*')
list.atend('a')
list.atend('/')
list.atend('*')
list.atend('d')
list.atend('o')
list.atend('c')
list.atend('t')
list.atend('o')
list.atend('r')
list.atend('*')
list.atend('A')
list.atend('w')
list.atend('a')
list.atend('y')
s=""
val=list.head

while val is not None:
    if (val.data=="*" or val.data=="/") :
        if s[len(s)-1]==" ":
            if val.ref.data is not None:
                s=s+val.ref.data.upper()
                val=val.ref

        else:
            s=s+" "
    else:
        s=s+val.data
        
    val=val.ref
print(s)
