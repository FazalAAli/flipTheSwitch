#!/bin/bash
cd /mnt/DE5E90795E904BE1/grub2
python3 linuxtowindows.py
echo "File Renaming Done... Starting reboot"
sleep 5
reboot