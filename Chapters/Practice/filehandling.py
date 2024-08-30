# f = open("file.txt")

# content = f.read()
# print(content)

# newcontent = content.upper()

# f = open("file.txt","w")
# f.write(newcontent)

# print(newcontent)

# f.close()



num = int(input("Enter a number: "))

f = open("file.txt")
content = f.read()
print("Previous highest number: ")
print(content)
f.close()

if content=="":
    f = open("file.txt","w")
    f.write(str(num))
    print("new highest number")
    f.close()

else:
    f = open("file.txt","w")

    if num>(int(content)):
      
        f.write(str(num))
        print("Given number is greater")

    elif int(content)>num:

        print("Given number is smaller")


    elif content==num:
        print("Equal")

    else:
        print("Error")

f.close()