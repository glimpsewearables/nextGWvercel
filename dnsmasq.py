import sys, time, os
import subprocess as sub
import logging


logging.basicConfig(filename='dnsmasq.log', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.info("logger setup")

WORKING_DIR = "/usr/src/app"

def getSsid():
        SSID = sub.check_output(['./nmcli'], shell=True)
        print(SSID[20:34])
        logger.info(SSID[20:34])
        return SSID[20:34]

        
def restartNetwork():
        print("restarting network")
        sub.call(['./nmcli radio wifi off'], shell=True)      
        time.sleep(5)
        sub.call(['./nmcli radio wifi on'], shell=True)
        print("turned network on")
        time.sleep(1)                     

def dnsMasq():
    time.sleep(4)
    os.chdir(WORKING_DIR)
    try:
        sub.Popen(['bash dnsmasq.sh'], shell=True)
        print("called dnsmasq")
        logger.info('called dndmasq')
        return "called dnsmasq"
    except RuntimeError as e:
        print(e)
        logger.error(str(e))
        return str(e)

def isHotspot():
        os.chdir(WORKING_DIR)
        connection = getSsid()
        if connection == 'balena-hotspot':
                print("Hotspot is active")
                logger.info("online")
                return True
        else:
                print("Hotspot is not active")
                logger.info("offline")
                logger.info(connection)
                return False

def changedMode(CURRENT_SSID, x):
    if x <= 10:
        time.sleep(.3)
        NEW_SSID = getSsid()
        if NEW_SSID != CURRENT_SSID: 
                print("changed")
                logger.info("change detected")
                if NEW_SSID == 'balena-hotspot':
                        print('hotspotmode')
                        logger.info("hotspot mode")
                        return True
        else:
            if NEW_SSID == 'ed to supervis':
                y = x + 1
                changedMode(NEW_SSID, y)
            else:   
                return False
    else:
        restartNetwork()
        sub.call(['./nmcli con up balena-hotspot'],shell=True)
        dnsMasq()

def bootUp():
        if isHotspot():
            logger.info(dnsMasq())

def main():
        bootUp()
        i = 0
        try:
                while i == 0:
                        CURRENT_SSID = getSsid()
                        if changedMode(CURRENT_SSID, 1):
                                restartNetwork()
                                dnsMasq()
                                time.sleep(10)
        except RuntimeError as e:
                logger.info(str(e))

                time.sleep(1)


main()