n=int(input("enter the no. of elements in array:  "))
arr=[]
arr_odd=[]
arr_even=[]
print("enter the numbers.")
for i in range(n):
    a=int(input("enter number "+str(i+1)+": "))
    arr.append(a)
    if(a%2==0):
        arr_even.append(a)
    else: 
        arr_odd.append(a)
print("Original array is: ", arr)
arr_even=sorted(arr_even)
arr_odd=sorted(arr_odd, reverse=True)
arr=arr_odd+(arr_even)
print("after changes : ",arr)
