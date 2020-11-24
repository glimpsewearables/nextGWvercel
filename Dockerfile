### Use Debian Buster for a recent `nmcli` version
###
FROM balenalib/rpi-debian-node

ENV PORT 3000

RUN install_packages python
RUN install_packages wireless-tools
RUN install_packages iw
### D-Bus calls needs to be directed to the system bus that the host OS is listening on
###
ENV DBUS_SYSTEM_BUS_ADDRESS unix:path=/host/run/dbus/system_bus_socket

### Install `nmcli` dependencies
###
RUN apt-get update \
    && apt-get install -y libnm0 libpolkit-agent-1-0

### `nmcli` will be available in the `/usr/src/app` folder
###
RUN rm -rf /usr/src/app

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

### Download and extract the `nmcli` utility
###
RUN mkdir nm-download \
    && chown -Rv _apt:root nm-download \
    && cd nm-download \
    && apt-get download network-manager \
    && dpkg -x $(ls) . \
    && cd .. \
    && mv nm-download/usr/bin/nmcli . \
    && rm -rdf nm-download

### Cleanup after downloading packages
###
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*


### Copy NextGW and install
COPY . /usr/src/app


RUN npm install \
    && npm run build


### Copy the start script executing `nmcli`
###
##DNS
RUN apt-get update
RUN apt-get install -y dnsmasq
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

#COPY dnsmasq.conf /etc/dnsmasq.conf

COPY start.sh .
COPY dnsmasq.sh /usr/src/app/dnsmasq.sh
COPY dnsmasq.py /usr/src/app/dnsmasq.py

EXPOSE 80

#Create hotspot
#RUN ./nmcli -f=SSID,BARS d wifi
#RUN ./nmcli con add type wifi ifname wlan0 con-name Hotspot autoconnect yes ssid glimpseCam
#RUN ./nmcli con modify Hotspot 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared
#RUN ./nmcli con modify Hotspot wifi-sec.key-mgmt wpa-psk
#RUN ./nmcli con modify Hotspot wifi-sec.psk "password"
### Run a `nmcli` command
###
RUN install_packages nano

CMD ["bash", "start.sh"]
