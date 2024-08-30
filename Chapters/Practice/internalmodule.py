import os
import time

path = "."

content = os.listdir(path)

for i in content:
    print(i)

command = "pwd"
os.system(command)


t1 = time.time()

for i in range(100):
    print(i)
time.sleep(3)

t2 = time.time()

t = t2-t1

print(t)

l = time.localtime()
print(l)
t3 = time.strftime("%y/%m/%d   %H:%M:%S",l)
print(t3)


command = "notify-send 'Hello-karan'"
os.system(command)