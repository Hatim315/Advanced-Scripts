import os,sys
from getpass import getuser
import platform
#print("(In Windows, target folder must be in C drive)")
Location=input("Give the location of the files.For example, Desktop/Folder or Downloads/Folder: ")
Type=input("Name of the file extension[txt/pdf/png and many more]: ")

Sys=platform.system()  # getting the operating system
usr=getuser()  # getting the current user's name
pwd=os.getcwd()   # getting the current working directory


if "linux"  in Sys.lower():
    #dir syntax for linux 
    dir=f"/home/{usr}/{Location}"
elif Sys.lower()=="windows":
    #dir syntax for windows
    dir=f"C://Users\\Public\\{usr}\\{Location}"
else:
    print("edit the code to work with your os")
    sys.exit()


def run(Type):
    #This function is responsible for renaming all the files in a folder
    try:
        arr=os.listdir()
        for i in range(len(arr)):
            if arr[i].split(".")[-1]==Type:
                os.rename(arr[i],f"{i+1}.{Type}")
        print("Sucess")
    except:
        print("Fail")

if pwd==dir:
    #if current directory is same as file location then execute the function
    run(Type)
else:
    #else change the directory to the location of file and then run the function
    os.chdir(dir)
    run(Type)