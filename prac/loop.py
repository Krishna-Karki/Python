a = int(input("Enter your age: "))
print("Your age is : ",a)

if(a>18):
    print("You can drive")
    #elif
else:
    print("You cannot drive")

    x = int(input("Enter number: "))
    match x:
        case 0:
            print("hello")
        case 1:
            print("hi")
        case _ :
            print(x)

name = "krishna"
for i in name:
    print(i)
    if(i=="a"):
        alpha=name.count("a")

for k in range(5):
    print(k+1)


i=0
while(i<=3):
    print(i)
    i =i+1

print("loop ended")

for i in range(10):
    print("5 X", i + 1, "=", 5 * (i + 1))
    if i == 5:
        break
    then
    continue
    