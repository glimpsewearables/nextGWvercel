import sys, time, os
import subprocess as sub
import logging


logging.basicConfig(filename='dnsmasq.log', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.info("logger setup")

WORKING_DIR = "/usr/src/app"

def getSsid():
	SSID = sub.check_output(['./nmcli'], shell=True)
	return SSID[20:34]

def changedMode(CURRENT_SSID):
	time.sleep(.5)
	NEW_SSID = getSsid()
	if NEW_SSID != CURRENT_SSID: 
		print("changed")
		logger.info("change detected")
		if NEW_SSID == 'balena-hotspot':
			logger.info("hotspot mode")
			return True
	else:
		return False

def dnsMasq():
    time.sleep(2)
    os.chdir(WORKING_DIR)
    try:
        dnsmasq = sub.call(['bash', 'dnsmasq.sh'])
        logger.info(dnsmasq)
        return dnsmasq
    except RuntimeError as e:
        print(e)
        logger.error(str(e))
        return str(e)

def online():
	os.chdir(WORKING_DIR)
	connection = sub.check_output(['./nmcli','networking', 'connectivity']).decode(sys.stdout.encoding)

	if connection[0:4] == 'full':
		logger.info("online")
		return True
	else:
		logger.info("offline")
		logger.info(connection)
		return False

def bootUp():
	if online() == False:
		logger.info(dnsMasq())
	
def main():
	bootUp()
	i = 0
	try:
		while i == 0:
			CURRENT_SSID = getSsid()
			if changedMode(CURRENT_SSID):
				time.sleep(1)
				dnsMasq()
				time.sleep(10)
	except RuntimeError as e:
		logger.info(str(e))

		time.sleep(1)
			
main()
