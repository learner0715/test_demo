a1, a2 = 0, 1
n=5
for i in range(n):
    c=a1+a2
    a1=a2
    a2=c
    print(c,end=" ")