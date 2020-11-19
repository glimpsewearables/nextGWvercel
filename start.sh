echo "Starting nextGW - $(date)"
cd /usr/src/app
npm run start &
#bash dnsmasq.sh &
python dnsmasq.py &
tail -f /dev/null