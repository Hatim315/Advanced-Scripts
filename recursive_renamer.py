import os

def renamer(path,format):
    """For renaming files recursively in all directories in a directory"""
    os.chdir(path)
    count=0
    l=[]
    for i in sorted(os.listdir(),key=lambda x:int(os.path.getctime(x))):
        if os.path.isdir(i):
            l.append(i)
        if format in i:
            count+=1
            os.rename(i,f"{count}.{format}")
    for j in l:
        renamer(os.path.join(path,j),format)
    print("Success")    

if __name__=="__main__":
    
    path=input("path to the folder: ")
    format=input("type of files img/Jpg/jpeg: ")
    renamer(path,format)
    