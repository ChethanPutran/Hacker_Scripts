import socket
from IPy import IP
import sys

#Range of ports to scan
startPort = 20
endPort = 30

class PortScanner:
    def __init__(self,target):
        self.target = self.checkIp(target)
        if(self.target == None):
            print("Unkown host {target}!")
            sys.exit()
            
        self.banners = []
        self.openPorts = []
    
    def scanForRange(self,startPort,endPort):
        #Checking for range of open ports
        try:
            # print('\n'+'[+] Scanning Target '+ str(self.target)+' ...')
            for port in range(int(startPort),int(endPort)):        
                self.portScanner(port) 
        except Exception as e:
            pass 
                    
    def checkIp(self,ip):
        #Checking whether user entered ip adress or url 
        try:
            IP(ip)
            return ip
        except Exception as e:
            try:
                return socket.gethostbyname(ip)
            except:
                return None

    def portScanner(self,port):
        port = int(port)
        try:
            #Creating socket
            soc = socket.socket()
            soc.settimeout(0.5)
            soc.connect((self.target,port))
            self.openPorts.append(port)
            try:
                banner = soc.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
                # print('[+] Open Port '+ str(port)+' : '+str(banner)+'\n')
            except Exception as e:
                self.banners.append(None)
            soc.close()
            
        except Exception as error:
            # print('[+] Port '+ str(port)+' is closed!\n')
            return None
           

if __name__ == '__main__':
       
    #Asking for client address and port to connect or scan
    targets = input("[+] Enter Target/s to Scan (split multiple targets with ',') : ")
    choice = input("1.Enter port to scan\n2.Enter range of ports to scan\n3.Exit\n")
    print(choice)
    
   
    while True:
        if "," in targets:
            targets = targets.split(',')
            print(targets)
        
            if(int(choice)==1):
                port = input('Enter Port: ')
                for target in targets:
                    scanner = PortScanner(target.strip(' '))
                    scanner.portScanner(port)
            elif(int(choice)==2):    
                for target in targets:
                    scanner = PortScanner(target.strip(' '))
                    scanner.scanForRange(startPort,endPort)
            else:
                quit()
        else:
            if(int(choice)==1):
                port = input('Enter Port: ')
                scanner = PortScanner(targets)
                scanner.portScanner(port)
            elif(int(choice)==2):   
                startPort = input('Enter Start Port: ')
                endPort = input('Enter End Port: ') 
                scanner = PortScanner(targets)
                scanner.scanForRange(startPort,endPort)
            else:
                sys.exit()



        
        
        
