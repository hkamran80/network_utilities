# Network Scanner

import subprocess
import socket
import json
import sys
import re

#base_ip = sys.argv[1] if len(sys.argv) > 1 else input("Base IP Address (example: 192.168.1): ")
base_ip_0 = socket.gethostbyname(socket.gethostname())
base_ip = base_ip_0[:-(len(base_ip_0.split(".")))]

max_ip = 255

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
			if "Request timeout" in p or "sendto" in p or "Host is down" in p:
				continue
			else:
				pluses += 1

		if pluses > len(ping_cmd)-2:
			return 1
		else:
			return 0

def mac_lookup(mac_addr):
	file = "macs.json"

	j = json.loads(open(file).read())

	try:
		return j[":".join(mac_addr.split(":")[:3])]
	except KeyError:
		return 0

def known(mac_addr):
	file = "known.json"

	j = json.loads(open(file).read())

	try:
		return j[mac_addr]
	except KeyError:
		return 0

def get_network():
	s = subprocess.Popen(["route", "-n", "get", "default"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("ascii")
	s_ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', s)

	arp = subprocess.Popen(["arp", "-n", "{}".format(s_ip[0])], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	arp_mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", arp[0].decode("ascii")).groups()[0]

	file = "networks.json"
	j = json.loads(open(file).read())

	try:
		return j[arp_mac]
	except KeyError:
		return "Unknown Network"

print("Scanning \"\033[94m{}\033[0m\"".format(get_network()))
print("="*40)

for ip in range(1, max_ip+1):
	ip_addr = base_ip + "." + str(ip)
	try:
		if ping(ip_addr) == 1:
			mac_addr = get_mac_addr(ip_addr)
			if mac_addr == "ff:ff:ff:ff:ff:ff":
				break
			else:
				ml = mac_lookup(mac_addr)
				known_mac = known(mac_addr)
				if ml == 0:
					if known_mac != 0:
						#print("0")
						print("{}: {} (--) ({})".format(ip_addr, mac_addr, known_mac))
					else:
						#print("1")
						print("{}: {} (--)".format(ip_addr, mac_addr))
				else:
					if known_mac == 0:
						#print("2")
						print("{}: {} ({})".format(ip_addr, mac_addr, ml))
					else:
						#print("3")
						print("{}: {} ({}) ({})".format(ip_addr, mac_addr, ml, known_mac))
		else:
			#print("{}: Offline".format(ip_addr))
			continue
	except subprocess.CalledProcessError:
		#print("{}: Offline".format(ip_addr))
		continue
