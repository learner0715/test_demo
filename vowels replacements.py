a = ['a','A','e','E','i','I','o','O','u','U']
b = 'heelou'
c = 0
for i in b:
    if i in a:
        c = i.replace("e","u")
        print(c, end="")
    else:
        print(i, end="")