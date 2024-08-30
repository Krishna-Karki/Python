def func(a,b):
   sum= a+b
   return sum

add = func(5,6)
print(add)

#recursive function

a = int(input("Enter a number: "))

def func(n):
    if(n==0):
        return 0
    return n + func(n-1)

add = func(a)
print(add)

#factorial


a = int(input("Enter a number: "))

def func(n):
    if(n==0):
        return 1
    return n * func(n-1)

mul = func(a)
print(mul)

