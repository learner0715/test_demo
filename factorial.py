num = 5 
factorial = 1
if num > 0:
    for i in range(1,num+1):
        factorial = factorial * i
        print(factorial)
else:
    print("{0} is not a psotive number".format(num))