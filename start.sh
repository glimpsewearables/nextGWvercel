echo "Starting nextGW - $(date)"
cd /usr/src/app
npm run start &

sleep 1

python dnsmasq.py &


cd /etc
rm localtime
ln -s /usr/share/zoneinfo/US/Pacific localtime


tail -f /dev/null
