import portscanner


targets = input("[+] * Enter Target/s to Scan for Vulnerable Open Ports : ")
portRanges = input("[+] * Enter range of ports to scan Eg. 20,30\n : ")
choice = input("1.Display Vulnerabilities\n2.Store output \n : ")

if(int(choice)==2):
     vulnFile = input("[+] * File path and name to store the output : ")

portRanges = portRanges.split(',')
targets = targets.split(',')
for target in targets:
    target = target.strip('\n').strip(' ')
    scanner = portscanner.PortScanner(target)
    startPort = portRanges[0].strip('\n').strip(' ').rstrip('\n') 
    endPort = portRanges[1].strip('\n').strip(' ')
    scanner.scanForRange(startPort,endPort)
    try:
        if (int(choice)==1):
            i=0
            for banner in scanner.banners:
                    content = '[!!] Vulnerable Banner for '+ target +' "'+ banner + '" On PORT: '+str(scanner.openPorts[i])+"\n"
                    print(content)
                    i+=1  
        elif(int(choice)==2):
            i=0
            with open(vulnFile,'a') as file:
                for banner in scanner.banners:
                    file.seek(0)
                    content = '[!!] Vulnerable Banner for '+ target +' "'+ banner + '" On PORT: '+str(scanner.openPorts[i])+"\n"
                    file.writelines(content)
                    i+=1            
        else:
            print("[!!!] Invalid Choice")   
    except Exception as e:
        print("Errrrorrrw")        