n=int(input("enter the no of items in your dictionary:  "))
d=dict()
for i in range(n):
    k=input("enter key for item no"+str(i+1)+":  ")
    val=int(input("enter value for it:  "))
    d[k]=val
l=d.items()
r=dict()
for k,val in l:
    if val not in r.values():
        r[k]=val
print("Dictionary with no duplicates is: ",r)
