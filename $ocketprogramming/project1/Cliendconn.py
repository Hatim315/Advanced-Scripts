#!/usr/bin/python3

import socket 
h='127.0.0.1'
p=3307
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    
    s.connect((h,p))
    
    
    
    while True:  
        try: 
           x=input("Me--")
           s.send(f"CLIENT:--{x}".encode("utf-8"))
           data=s.recv(2024)
           print((data).decode("utf-8"))
           if data=="b''":break
        except:
            print("an error occured connection is closing")
            break
            