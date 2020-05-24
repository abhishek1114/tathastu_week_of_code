a=input("enter string:  ")
al=list(a)
print(al)
final=[]
for i in al:
    if i not in final:
        final.append(i)
print("list without duplicate  ",final)
