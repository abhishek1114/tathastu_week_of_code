num=int(input("enter a number:  "))
if num%2==0:
    print("It is an even number.")
else:
    print("It is an odd number.")
c=0
for i in range(1,num+1):
    if num%i==0:
        c=c+1
if c==2:
    print("It is a prime number")
rev=0
cp=num
while cp!=0:
    r=cp%10
    rev=rev*10+r
    cp=cp//10
if rev==num:
    print("It is a pallindrome number.")
cp1=num
s=0
while cp1!=0:
    r=cp1%10
    s=s+(r*r*r)
    cp1=cp1//10
if s==num:
    print("It is an armstrong number.")
