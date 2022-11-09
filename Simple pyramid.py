#--------------simple pyramid-------------------#
"""
def python(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end=" ")
        print("\r")
n = int(input())
python(n)
"""

#---------------using list------------------------#
"""
def python(n):
    mylist = []
    for i in range(1, n+1):
        mylist.append("* " * i)
    print("\n".join(mylist))
n = int(input())
python(n)
"""

#---------------after 180 rotation----------------#
"""
def python(n):
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k-2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
n = int(input())
python(n)
"""

#-------------printing triangle-------------------#

def triangle(n):
    k = n-1
    for i in range(0,n):
      for j in range(0,k):
          print(end=" ")
      k = k-1
      for j in range(0, i+1):
        print("*", end=" ")
      print("\r")
n = int(input())
triangle(n)