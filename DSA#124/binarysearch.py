def binarysearch(list,x):
    low=0
    high=len(list)
    while(low<high):
        mid=(low+high)//2
        if list[mid]==x:
            return mid
        elif x<=list[mid]:
            high=mid
        else:
            low=mid
    return "element is not found"
list=[3,4,5,6]
print(binarysearch(list,0))
