n=int(input("enter the no of items in your dictionary:  "))
d=dict()
for i in range(n):
    k=input("enter key for item no"+str(i+1)+":  ")
    val=int(input("enter value for it:  "))
    d[k]=val
l=[]
l=d.values()
l=sorted(l)
print("second max. element in dictionary is: ",l[-2])
