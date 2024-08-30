import os

#specify the directory you want to list
directory_path = '/home/karan/Documents/'

#use the os module to the list the directory content
contents = os.listdir(directory_path)


#print each file and directory name
for item in contents:
    print(item)