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
            # a=1
            while val is not None:
                print(val.data,end=" ")

                val=val.ref
                # a+=1
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
    def delete_new(self,data):
        val=self.head
        while val is not None:
            if val.data==data:
                val.data="empty"
            val=val.ref
    def insert_new(self,data):
        val=self.head
        val1=self.head
        a=1
        newnode=Node(data)
        while val is not None:
            if val.data=="empty":
                print("you are allocated to the table no",a)
                val.data=data
                a+=1
                val=val.ref
                return
        a=1
        if self.head==None:
            
            print("you are allocated to table",a)
            a+=1
            self.head=newnode
        else:
            while val1.ref is not None:
                val1=val1.ref
                a+=1
            val1.ref=newnode
        print("you are allocated to table",a)
        return

        
            
            


l1=linkedlist()
# class bakehouse:
#     def __init__(self,l1):
#         self.l1=l1
#     def get_occupied_table_list(self):
#         self.l1.listprint()
#     def allocate_table(self,data):
#         self.l1.insert_new(data)
#     def deallocate_table(self,data):
#         self.l1.delete_new(data)
# b=bakehouse(l1)
# b.allocate_table("ravi")
# b.allocate_table("sumu")
# b.allocate_table("sab")
# b.deallocate_table("sumu")

# b.get_occupied_table_list()
l1.insert_new("ravi")
l1.insert_new("subu")
# l1.delete_new("ravi")
l1.insert_new("hmmm")
l1.listprint()




