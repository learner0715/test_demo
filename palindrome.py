a = input()
b = a[::-1]
if b == a:
    print("{0} is a palindrome".format(a))
else:
    print("{0} is not a palindrome".format(a))