l=["a","b","c","d"]
l2=["a1","b2",None,"d2"]
l2.reverse()
for i in range(0, len(l)):
    if l[i]==None:
        print(" "+l2[i],end="")
    elif l2[i]==None:
        print(l[i]+" ",end="")
    else:
        print(l[i]+l2[i],end="")