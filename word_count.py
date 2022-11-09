a = input()
l1=a.lower()
s=l1.split()
b=input()
l2=b.lower()
c=0
if l2 in s:
  for i in s:
    if i == l2:
        c += 1
  print(c)
else:
  print("word not found")
