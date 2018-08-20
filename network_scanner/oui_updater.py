# OUI Updater

import requests
import json

oui = requests.get("http://standards-oui.ieee.org/oui/oui.txt").text

def prefix(oui_obj):
	macpre = ""

	for s in oui_obj.split("\n")[0].split()[0].split("-")[:-1]:
		try:
			macpre = macpre + str(int(s)) + ":"
		except Exception as e:
			macpre = macpre + str(s).lower() + ":"

	try:
		macpre = macpre + str(int(oui_obj.split("\n")[0].split()[0].split("-")[-1]))
	except Exception as e:
		macpre = macpre + str(oui_obj.split("\n")[0].split()[0].split("-")[-1]).lower()

	#print(macpre)
	return macpre

def manu_mac(oui_obj):
	return oui_obj.split("\t")[2].split("\n")[0].strip()
#while True:
#	print(prefix(oui.split("\n\n")[int(input("Number: "))]))

ouis = {}

for oui in oui.split("\n\n")[1:]:
	ouis[prefix(oui)] = manu_mac(oui)

print(ouis)
with open("macs.json", "w") as macs:
	macs.write(json.dumps(ouis))
