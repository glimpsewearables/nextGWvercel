echo "Starting nextGW - $(date)"
cd /usr/src/app
python dnsmasq.py &
sleep 1
npm run start &
tail -f /dev/null