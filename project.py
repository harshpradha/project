import socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
#SOCKET LIBRARY=("In the short word we can say connection less library") 
ip_add='192.168.1.4' 
# port=9999
pura_add=(ip_add,port)
message=input("chita hi khh de 😉")
encript_msg=message.encode('ascii')
s.sendto(encript_msg,pura_add) 



import socket
h=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #b size= limit dete h
ip_add='192.168.1.49'
port=588
pura_add=(ip_add,port)
h.bind(pura_add)
while True:
    message=h.recvfrom(150)
    print(message)
    data_massage=message[0]
    find_ms=data_massage.encode("ascii")
    print(find_ms)