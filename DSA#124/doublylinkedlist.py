class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Dlinkedlist:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        return False
    def insert_atbegin(self,number):
        newnode=Node(number)
        if self.isempty():
            self.head=newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        val=self.head
        while val.next is not None:
            print(val.data,"-->",end=" ")
            val=val.next
        print(val.data)
    def insert_atindex(self,number,a):
        if a==0:
            self.atbegin(number)
        else:
            newnode=Node(number)
            val=self.head
            c=0
            var=self.head
            while var is not None:
                var=var.next
                c+=1
            if a<=c:
                for i in range(0,a-1):
                    val=val.next
                newnode.prev=val
                newnode.next=val.next
                val.next=newnode
            else:
                print("The node canot be linked")
    def insert_atend(self,number):
        if self.isempty():
            self.atbegin(number)
        else:
            val=self.head
            while val.next is not None:
                val=val.next
            newnode=Node(number)
            val.next=newnode
    def delete_from_end(self):
        val=self.head
        while val.next.next is not None:
            val=val.next
        # print(val.data)
        val.next=None
    def delete_from_start(self):
        if self.isempty():
            print("Linkedlist is empty we can't delete")
        else:
            val=self.head.next
            self.head.next.prev=None
            self.head=val
    def delete_value(self,number):
        if number==self.head.data:
            self.delete_from_start()
            return 
        else:
            val=self.head
            while val is not None:
                if val.data==number:
                    if val.next is not None:
                        val.prev.next=val.next
                        return
                    else:
                        self.delete_from_end()
                        return
                val=val.next
            print("The value is not present in linkedlist")
        
node=Dlinkedlist()
node.insert_atbegin(5)
node.insert_atbegin(4)
node.insert_atbegin(3)
node.insert_atindex(6,3)
node.insert_atend(7)
# node.delete_from_start()
node.delete_value(9)
print()
node.printlist()



