#!/usr/bin/python3
import os,shutil

def organiser(path):
    os.chdir(path)
    files=os.listdir()
    extensions={
        ("pdf","docx","pptx"):"Files",
        ("zip","tar","rar"):"Archive",
        ("mp3","wav"):"Music",
        ("jpeg","jpg","img","png","heic"):"Images",
        ("mkv","mp4"):"Movies"

               }
   
    for i in files:
      if os.path.isfile(i): 
         
         f=i.split(".")[-1]
         
         for j,k in extensions.items():
             if f in j:
                #os.makedirs(k,exist_ok=True)
                if not os.path.exists(k):
                    os.mkdir(k)
                shutil.move(i, k)
    print("Done!!")
if __name__=="__main__":
    path=input("Give the path of the folder ou want to organise: ")
    organiser(path)
