x = 30
print("Factors of {0} is :".format(x))
for i in range(1,x+1):
    if (x % i)==0:
        print(i,end=" ")