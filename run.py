import os
import sys
import time
import requests
os.system('clear')
os.system('rm -rf list.txt')
os.system('1778 -u > list.txt')
uid = open('list.txt', 'r')
for j in uid:
    sp = j.split()

def chk():

  uuid = str(os.geteuid()) + str(os.getlogin()) 

  id = "|".join(uuid)

  print("\n\n\x1b[37;1m YOUR ID : \033[94m"+id) 

  try: 

    httpCaht = requests.get("").text 

    if id in httpCaht: 

      print("\033[92m YOUR ID IS ACTIVE.........\033[97m") 

      msg = str(os.geteuid()) 

      time.sleep(1) 

      pass 

    else: 

      print("\033[0;96m Id kat active nya Tkaya bo Active krdn NAME bnera bo telegram @") 

      os.system('xdg-open https://t.me/s4m0_cracker1

      time.sleep(1) 

      sys.exit() 

  except: 

    sys.exit() 

    if name == 'main': 

     print (logo)

     chk() 

     
     
chk()
