#coding: utf -8

'''Importando a biblioteca Socket que será usada pra fazermos as conexões'''
import socket


'''a variavel ip vai gravar o endereço que voce digitar pra testar se as portas estão abertas'''
ip = raw_input("Ip ou Endereço :")


'''variavel pergunta recebe s ou n '''
pergunta = raw_input("Deseja scanear apenas as portas mais usada ? S/N :")

'''lista de portas mais usadas, não tem todas por isso adicionei uma funçao que permite escolher quais quer escanear'''
pt = [18, 20, 21, 22 , 23, 24, 25, 25, 80, 81, 118, 120 , 122 , 443, 1033]

'''range caso voce queira scanear todas as portas'''
ports = range(65535)

'''definindo a função contador '''
''' essa função pede um numero de portas que voce deseja scanear'''
''' ela cria uma lista de portas com essas portas que voce digitou'''
''' e por fim. testa se essas portas estão abertas'''

def contador(ip):
    numero = (int(raw_input("Quantas Portas deseja scanear ? :")))
    contadora = 0
    pu = []
    while contadora < numero:
        pu.append(int(raw_input("Informe ""a "+str(contadora + 1)+" PORTA :")))
        contadora += 1
    testar(ip, pu)


'''aqui definimos a função principal do progama,onde o teste acontece''' 
def testar(ip, ports):
 
    '''pra cada porta dentro da variavel ports'''
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #cria um socket como s
        s.settimeout(1)              #define o timeout, quanto menor o timeout, mais rapido o scan, mas isso depende da velocidade da sua internet
        resp = s.connect_ex((ip, port))   #aqui ele se conecta ao ip, que foi guardado na variavel ip e na porta que voce escolheu

        if resp == 0: #aqui ele compara, o conect_ex  retorna 0 pra conexão que deu certo , e 1 pra que deu errado ,se for 0 ele vai printar a mensagem abaixo em verde
            print '\033[32m'+'==>> Porta '+str(port)+' Aberta <<==' +'\033[0;0m'

def perguntas(ip, pt, ports, pergunta):    #definindo as perguntas'
    if pergunta == 's': #se a priemira pergunta for igual a sim ele vai passar o ip que voce digitou e a lista de portas mais usadas "pt" 
        testar(ip, pt)

    if pergunta == 'n':  #se for igual a "n", ele vai fazer outra pergunta
        var1 = raw_input ('\033[31m'+'Deseja scanear TODAS as portas de '+ip+' S/N :''\033[0;0m')
        if var1 == 's':          #se a resposta pra pergunta for 's', ele vai testar o range de todas as portas possiveis
            testar(ip, ports)
        else:
            contador(ip)   #se todas as respostas forem 'n' ele vai chamar a variavel contador, perguntar quantas portas voce qquer scanear, perguntar quais portas são essas
                           #e por fim testar essas portas e exibir o resultado do scan na tela :)

perguntas(ip, pt ,ports, pergunta)
