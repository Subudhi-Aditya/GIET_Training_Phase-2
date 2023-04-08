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
        # i=0
        while(current is not None):
            val=current.ref
            current.ref=prev
            prev=current
            current=val
            # i+=1
        self.head=prev

        



        

l1=linkedlist()
l1.atend("sun")
l1.atend("mon")
# l1.atend("tue")
# l1.atend("fri")
# l1.delete_at_value("thurs")

# l1.atsome("wed",3)

l1.listprint()
l1.reverse()
l1.listprint()
# l1.listprint()
# l1.atsome("hi")
# l1.listprint()