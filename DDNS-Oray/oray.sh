#!/bin/bash
domain=""
user=""
pwd=""
/usr/bin/curl "http://$user:$pwd@ddns.oray.com/ph/update?hostname=$domain"
cd /mnt/main/Main/Software/IP && python IPAlarm.py
