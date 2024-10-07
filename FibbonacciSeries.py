a=int(input(""))
b=1
c=1
print(b,c,end=" ")
for i in range(a-2):
    k=c
    c=b+c
    b=k
    print(c,end=" ")