echo "Starting nextGW - $(date)"
cd /usr/src/app
python dnsmasq.py &
sleep 1
npm run start &

echo "America/Los_Angeles" > /etc/timezone
dpkg-reconfigure tzdata

tail -f /dev/null