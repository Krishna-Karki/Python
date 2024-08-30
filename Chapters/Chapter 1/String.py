name = input("Enter your name: ")
count = len(name)
print(f"The length of the string '{name}' is {count}.")
nameshort = name[0:4]
print(name.endswith("rki"))

#a = (1,2,False,"Krishna")  tuple cannot change
#b= [] list can change b[0] = 5 which will replace the first details

marks = []
f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
marks.sort()
print(marks)
