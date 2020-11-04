echo "Starting nextGW - $(date)"
sleep 10
cd /usr/src/app
npm run start &
python dnsmasq.py &
tail -f /dev/null