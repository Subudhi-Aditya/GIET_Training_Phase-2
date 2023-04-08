text="the sun rises in the east"
voc=["sun","in","east","doctor","day"]
t=list(text.split())
l=set()
for i in t:
    if i not in voc:
        l.add(i)
print(l)
