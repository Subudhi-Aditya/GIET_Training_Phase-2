class Compartments:
    def __init__(self,name,tsc,nop):
        self.name=name
        self.tsc=tsc
        self.nop=nop
    def get_tsc(self):
        return self.tsc
    def get_nop(self):
        return self.nop
    def get_cname(self):
        return self.name
class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        return False
    def insert_at_end(self,d):
        newnode=Node(d)
        if self.head==None:
            self.head=newnode
        else:
            val=self.head
            while val.ref is not None:
                val=val.ref
            val.ref=newnode
    

c1=Compartments("general",400,20)
c2=Compartments("sl2",300,160)
c3=Compartments("sl3",300,140)
c4=Compartments("sl4",300,165)
c5=Compartments("sl5",300,170)
clist=linkedlist()
clist.insert_at_end(c1)
clist.insert_at_end(c2)
clist.insert_at_end(c3)
clist.insert_at_end(c4)
clist.insert_at_end(c5)


    
    
class Train:
    def __init__(self,tname,clist):
        self.tname=tname
        self.clist=clist
    def get_name_train(self):
        return self.tname
    def get_compartment_list(self):
        return self.clist
    def check_vacancy(self):
        a=0
        val=clist.head
        while val is not None:
            if ((val.data.get_tsc())-(val.data.get_nop())) > ((val.data.get_tsc())//2):
                a+=1
            val=val.ref
        return a
    def count_compartments(self):
        val=clist.head
        len=0
        while val is not None:
            len+=1
            val=val.ref
        return len
     
        

t=Train("saptagiri express",clist)
print("the no of vacany comartments are",t.check_vacancy())
print("the total no of compartments are ",t.count_compartments())
    


    