a = int(input("Enter your age: "))

if(a>=18):
    print("You are allowed to drive")
elif(a<0 | a==0):
    print("You are entering an invalid age")
else:
    print("you are below the driving age.")