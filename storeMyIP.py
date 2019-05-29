import requests
from fabric.connection import Connection

IP_file = 'myIP'

ipaddr = requests.get("https://api.ipify.org").text
print(ipaddr)

with open(IP_file, 'w') as f:
    f.write(ipaddr)
    f.truncate()

with Connection('ssh.mayeur.be', user='mayeur.be') as c:
    c.put(IP_file, remote=IP_file)

