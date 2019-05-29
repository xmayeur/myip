import warnings
import requests
from fabric.connection import Connection
import sys
import os
if os.name != 'nt':
    sys.path.insert(0, '\conf')
from config import *

warnings.filterwarnings("ignore")
ipaddr = requests.get("https://api.ipify.org").text
print(ipaddr)

with open(IP_file, 'w') as f:
    f.write(ipaddr)
    f.truncate()

with Connection(HOST, user=USER) as c:
    c.put(IP_file, remote=IP_file)

