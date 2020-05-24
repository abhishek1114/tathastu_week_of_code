def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

lst1 = [] 
lst2= []
n1 = int(input("Enter number of elements in list 1 : ")) 
n2 = int(input("Enter number of elements in list 2 : "))
print("enter elements in list 1:  ")
for i in range(0, n1): 
    ele = int(input()) 
    lst1.append(ele) 
      
print("enter elements in list 2:  ")
for i in range(0, n2): 
    ele = int(input()) 
    lst2.append(ele)
    
print(intersection(lst1, lst2)) 
