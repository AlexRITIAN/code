import os

newDir = input("Enter name of dir : ")
try:
    os.chdir("..")
except WindowsError:
    print("Can't change to Directory")
try:
    os.mkdir(newDir)
except WindowsError:
    print(newDir + "Directory Exists")

dirList = os.listdir(os.getcwd())
print(dirList)