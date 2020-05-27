def knapsack(wt, lst):
    if wt == 0 or len(lst) == 0:
        return 0
    if len(lst) == 1:
        if lst[0][0] > wt:
            return 0 
        return lst[0][1]  
    if lst[0][0] > wt:
        return knapsack((wt, lst[1:]))
    return max(lst[0][1] + knapsack(wt - lst[0][0], lst[1:]), knapsack(wt, lst[1:]))
n =  int(input("Enter the number of items you want to enter: "))
lst = []
for i in range(n):
    wt = int(input("Enter the weight for item number " + str(i + 1) + ": "))
    value = int(input("Enter the value for item number " + str(i + 1) + ": "))
    lst.append((wt,value))
wt = int(input("Enter the value of weight capacity: "))
print("The maximum value for the given weight value pair is ", knapsack(wt, lst))
