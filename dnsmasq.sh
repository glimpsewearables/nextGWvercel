echo "Starting dnsmasq - $(date)"
sleep 10
dnsmasq \
  --address=/#/10.42.0.1 \
  --dhcp-range=10.42.0.1,10.42.0.254 \
  --dhcp-option=option:router,10.42.0.1 \
  --interface=wlan0 \
  --keep-in-foreground \
  --bind-interfaces \
  --except-interface=lo \
  --conf-file \
  --no-hosts \
  --log-facility=-


tail -f /dev/null