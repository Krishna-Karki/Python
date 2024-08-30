list = [1, "karan",True,7.8]
print(list)

for i in list:
    print(i,end="\t")

list.append("krishna")
print(list)

list.insert(3,False)
print(list)

list.remove("krishna")
list.pop()
print(list)

