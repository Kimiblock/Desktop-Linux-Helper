#!/bin/bash
sudo pacman -S cups
sudo systemctl enable --now cups.service cups.socket
sudo pacman -S avahi
sudo systemctl enable --now avahi-daemon.service
echo '''
# Name Service Switch configuration file.
# See nsswitch.conf(5) for details.

passwd: files systemd
group: files [SUCCESS=merge] systemd
shadow: files systemd
gshadow: files systemd

publickey: files

hosts: mymachines mdns_minimal [NOTFOUND=return] resolve [!UNAVAIL=return] files myhostname dns
networks: files

protocols: files
services: files
ethers: files
rpc: files

netgroup: files
''' >temp.file
sudo mv temp.file /etc/nsswitch.conf
sudo pacman -S print-manager system-config-printer
if [ `pacman -Q | grep yay` ]; then
    yay -S hplip hplip-plugin
else
    sudo pacman -S hplip
    hp-plugin
fi
