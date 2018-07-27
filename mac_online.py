# MAC Online

import subprocess
import socket
import sys
import re

base_ip_0 = socket.gethostbyname(socket.gethostname())
base_ip = base_ip_0[:-(len(base_ip_0.split(".")))]

mac_scanned = sys.argv[1] if len(sys.argv) > 1 else input("MAC: ")

def get_mac_addr(ip_address):
	mac_cmd = subprocess.check_output(["arp", "-n", ip_address]).decode("ascii")

	return re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", mac_cmd).groups()[0]

def ping(ip_address):
	ping_cmd = subprocess.check_output(["ping", ip_address, "-t", "2"]).decode("ascii").split("\n")[1:][:-6]

	pluses = 0

	if "ping: sendto: Host is down" in ping_cmd:
		return 0
	else:
		for p in ping_cmd:
			if "Request timeout" in p or "sendto" in p:
				continue
			else:
				pluses += 1

		if pluses > len(ping_cmd)-2:
			return 1
		else:
			return 0

if __name__ == "__main__":
	for ip in range(1, 255):
		ip_addr = base_ip + "." + str(ip)
		try:
			if ping(ip_addr) == 1:
				print("{}: --".format(ip_addr))
				if get_mac_addr(ip_addr) == mac_scanned:
					print("{}: MAC is online!".format(ip_addr))
					break
			else:
				continue
		except subprocess.CalledProcessError:
			continue
else:
	for ip in range(1, 255):
		ip_addr = base_ip + "." + str(ip)
		try:
			if ping(ip_addr) == 1:
				if get_mac_addr(ip_addr) == mac_scanned:
					print("{}".format(ip_addr))
					break
			else:
				continue
		except subprocess.CalledProcessError:
			continue
