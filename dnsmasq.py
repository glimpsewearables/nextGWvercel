import sys, time, os
import subprocess as sub

WORKING_DIR = "/usr/src/app"

def getIp():
	IP_ADRESS = sub.check_output(['hostname','-I'], shell=True).decode(sys.stdout.encoding)
	IP_ADRESS = IP_ADRESS.split(" ", 1)
	return IP_ADRESS[0]

def changed(CURRENT_IP_ADRESS):
	time.sleep(5)
	NEW_IP_ADRESS = getIp()
	if NEW_IP_ADRESS != CURRENT_IP_ADRESS:
		return True
	else:
		return False

def dnsMasq():
	time.sleep(2)
	os.chdir(WORKING_DIR)
	sub.call(['bash', 'dnsmasq.sh'], shell=True)
	

def online():
	os.chdir(WORKING_DIR)
	connection = sub.check_output(['./nmcli','networking', 'connectivity']).decode(sys.stdout.encoding)

	if connection[0:4] == 'full':
		print("online")
		return True
	else:
		print("offline")
		print(connection)
		return False

def bootUp():
	online()
	dnsmasq = sub.check_call(['bash', 'dnsmasq.sh'], shell=True)
	print dnsmasq
	
def main():
	bootUp()
	i = 0
	while i == 0:
		CURRENT_IP_ADRESS = getIp()
		if changed(CURRENT_IP_ADRESS) and online() == False():
			dnsMasq()
			print ("activate DNS")
		
			
main()