#!/bin/bash
rm -f /etc/udev/rules.d/70-persistent-net.rules
rm -f /etc/sysconfig/network-scripts/ifcfg-eth1
/etc/init.d/network restart

# remove existig entry, if any
sed -i '/'master1'$/ d' /etc/hosts
# add a new one
echo "192.168.102.11	master1" >> /etc/hosts

sed -i '/'master1.1'$/ d' /etc/hosts
echo "192.168.102.111	master1.1" >> /etc/hosts

sed -i '/'master1.2'$/ d' /etc/hosts
echo "192.168.102.112	master1.2" >> /etc/hosts


sed -i '/'slave1'$/ d' /etc/hosts
echo "192.168.102.21	slave1" >> /etc/hosts

sed -i '/'jarvis.slave2'$/ d' /etc/hosts
echo "192.168.102.22	slave2" >> /etc/hosts
