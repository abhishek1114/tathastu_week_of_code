def change(l):
    for j in range(n-1):
        l[j]=max(l[j+1 : ])
    return l
n=int(input("Enter the size of list:  "))
print("Enter elements in list.")
lst=[]
for i in range(n):
    a=int(input("enter element "+str(i+1)+" in list:  "))
    lst.append(a)
lst=change(lst)
print("new list is: ",lst)
