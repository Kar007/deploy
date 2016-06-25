#!/bin/sh
/bin/ping 192.168.10.1 -w 1 -c 1 $2>/dev/null
ret=$?

if [ $ret -ne 0 ]
    then
    /usr/bin/pkill ppp
    /usr/sbin/pppd call vpn 
    /bin/sleep 15
    /sbin/route add -net 192.168.10.0 netmask 255.255.255.0 dev ppp0
    sleep 2
    route add -net 192.168.10.0 netmask 255.255.255.0 gw 192.168.10.215 dev ppp0
    sleep 2
    route add -net 192.168.30.0 netmask 255.255.255.0 gw 192.168.10.215 dev ppp0
fi
