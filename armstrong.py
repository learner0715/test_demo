a = int(input())
c = 0
b = str(a)
for i in b:
    d = int(i)
    c += d ** 3
if c == a:
    print("{0} is an Armstrong number".format(a))
else:
    print("{0} is not an Armstrong number".format(a))
