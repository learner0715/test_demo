num = int(input())
if num > 0:
    if (num % 2)==0:
        print("Number {0} is Even".format(num))
    else:
        print("Number {0} is Odd".format(num))
else:
    print("Enter a Positive Number")