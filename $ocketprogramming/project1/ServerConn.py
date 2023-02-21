import socket
h='127.0.0.1'
p=3307
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((h,p))
    
    s.listen()
    
        
        
    while True:
        conn,addr=s.accept()
        with conn as c:  
            data=c.recv(1024)

            print(data.decode("utf-8"))
            inp=input("Me--")
            c.send(f'ADMIN:--{inp}'.encode("utf-8"))
            