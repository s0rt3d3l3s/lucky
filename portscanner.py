#coding: utf -8

import socket

ip = raw_input("Ip ou Endereço :")

pergunta = raw_input("Deseja scanear apenas as portas mais usada ? S/N :")

pt = [18, 20, 21, 22 , 23, 24, 25, 25, 80, 81, 118, 120 , 122 , 443, 1033]

ports = range(65535)

def contador(ip):
    numero = (int(raw_input("Quantas Portas deseja scanear ? :")))
    contadora = 0
    pu = []
    while contadora < numero:
        pu.append(int(raw_input("Informe ""a "+str(contadora + 1)+" PORTA :")))
        contadora += 1
    testar(ip, pu)

def testar(ip, ports):
 
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        s.settimeout(1)              
        resp = s.connect_ex((ip, port))   

        if resp == 0:
            print '\033[32m'+'==>> Porta '+str(port)+' Aberta <<==' +'\033[0;0m'

def perguntas(ip, pt, ports, pergunta):   
    if pergunta == 's':
        testar(ip, pt)

    if pergunta == 'n': 
        var1 = raw_input ('\033[31m'+'Deseja scanear TODAS as portas de '+ip+' S/N :''\033[0;0m')
        if var1 == 's':         
            testar(ip, ports)
        else:
            contador(ip)  

perguntas(ip, pt ,ports, pergunta)
