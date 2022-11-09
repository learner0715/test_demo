num = int(input())
if num > 0:
  for i in range(1,num+1):
      print(i, "*", num, "=", i*num)
else:
  print("Enter a positive number ")