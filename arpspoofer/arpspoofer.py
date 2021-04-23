victimIp = '192.168.0.102'
routerIpAddress = victimIp.split('.')
routerIpAddress[3] = '1'

j='.'.join(routerIpAddress)

print(j)