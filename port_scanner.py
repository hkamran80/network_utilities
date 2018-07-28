# Port Scanner

from datetime import datetime
import subprocess
import socket
import sys

subprocess.call('clear', shell=True)

ports = []

remoteServer = sys.argv[1] if len(sys.argv) > 1 else input("Remote Server IP: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("="*60)
print("Scanning {}".format(remoteServerIP))
print("="*60)

t1 = datetime.now()

try:
    for port in range(1, sys.argv[2] if len(sys.argv) > 2 else 10000):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
            ports.append(port)
        sock.close()
except KeyboardInterrupt:
    print("Scanning canceled")
    sys.exit()
except socket.gaierror:
    print("Unable to resolve hostname")
    sys.exit()
except socket.error:
    print("Unable to connect to remote server")
    sys.exit()

t2 = datetime.now()

total_time = t2 - t1

print("Port scanning took {} to complete.".format(total_time))
