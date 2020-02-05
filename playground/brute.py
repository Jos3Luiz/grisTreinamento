#!/usr/python

"""<form method="POST" action="login_process.php">
  Username:<br>
  <input type="text" name="username"><br>
  Password:<br>
  <input type="text" name="password"><br><br>
  <input type="submit" value="Submit">
</form>"""



import request
#http for humans, pff import socket and write http on hand is much better


def tryPasswd(password,username):

    url="http://192.168.0.49:8080/login_process.php"
    myobj= {'name':username,'password':password}
    x = requests.post(url,data=obj)
    return x.text

tryPasswd("esoj","esoj")
    


