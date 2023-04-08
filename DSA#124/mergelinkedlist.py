class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def listprint(self):
        val=self.head
        c=0
        if self.head==None:
            print("LinkedList is empty")
        else:
            while val is not None:
                print(val.data,end=" ")

                val=val.ref
            print()
    def atbegin(self,data):
        newnode=Node(data)
        # val=self.head
        newnode.ref=self.head
        self.head=newnode
    def atend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            val=self.head
            while val.ref is not None:
                val=val.ref
            val.ref=newnode
    def atsome(self,data,a):
        newnode=Node(data)
        val=self.head
        val1=self.head
        a1=0
        while val1 is not None:
            val1=val1.ref
            a1=a1+1
        for i in range(a-1):
            if val.ref is not None:
                val=val.ref
            else:
                break
        if a<=a1:

            if val.ref is not None:

                newnode.ref=val.ref
                val.ref=newnode
            else:
                self.atend(data)
        else:
            print("desired node cant be linked")
    def delete_at_begin(self):
        val=self.head
        self.head=val.ref
    def delete_at_end(self):
        val=self.head
        while(val.ref.ref is not None):
            val=val.ref
        val.ref=None
    def delete_at_value(self,x):
        if self.head.data==x:
            # val=self.head
            self.head=self.head.ref
        else:
            val=self.head
            while(val.ref is not None):
                if val.ref.data==x:
                    val.ref=val.ref.ref
                    return
                val=val.ref
            if val.ref==None:
                print("The desired value is not present")
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            val=current.ref
            current.ref=prev
            prev=current
            current=val
        self.head=prev

l1=linkedlist()
l1.atend(1)
l1.atend(2)
l1.atend(4)
l1.atend(3)
l1.atend(5)
l1.listprint()
l2=linkedlist()
l2.atend(9)
l2.atend(8)
l2.atend(11)
l2.listprint()
n=int(input())
val=l1.head
for i in range(0,n-1):
    val=val.ref
val1=l2.head
while val1.ref is not None:
    val1=val1.ref
val1.ref=val.ref
val.ref=l2.head
l1.listprint()

