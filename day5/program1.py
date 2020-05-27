def rep(n):
    if(n==0):
        return 0
    d=n%10
    if d==0:
        d=5
    return(rep(int(n/10))*10+d)
n=int(input("enter a number:  "))
print(rep(n)
