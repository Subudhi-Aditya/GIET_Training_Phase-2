def linearsearch(list1,x):
    for i in range(0, len(list1)):
        if list1[i]==x:
            return "the element is found at index of",i
    return "the element is not found" 
list1=[2,3,1,4,7]
x=7
print(linearsearch(list1,x))
