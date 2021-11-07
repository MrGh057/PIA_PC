#! /bin/bash

sudo nmap -sS --min-rate 5000 -vvv -n -Pn $1 -oG nmap.txt
