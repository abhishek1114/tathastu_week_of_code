from itertools import permutations
st=input("enter a string:  ")
perms = [''.join(p) for p in permutations(st)]
print(perms)
