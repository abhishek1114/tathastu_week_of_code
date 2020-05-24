s=0
sp=6
for i in range(1,5):
    for j in range(1,s+1):
        print(" ", end="")
    s=s+1 
    print("*",end="")
    for k in range(1,sp+1):
        print(" ",end="")
    sp=sp-2
    print("*")
s=3
sp=0
for i in range(1,5):
    for j in range(1,s+1):
        print(" ", end="")
    s=s-1 
    print("*",end="")
    for k in range(1,sp+1):
        print(" ",end="")
    sp=sp+2
    print("*")
