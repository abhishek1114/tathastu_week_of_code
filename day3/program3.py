a=input("enter string:  ")
final=""
for i in a:
    if i not in final:
        final=final+i
print("String without duplicate letters: ",final)
