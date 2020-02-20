#!/bin/python3

#wmctrl -c chrome
#kill $(ps aux | grep "chrome") 
pkill --oldest --signal TERM -f chrome 

python /home/nemesis/Desktop/code/automation/test/login.py #/home/nemesis/Desktop/code/automation/test/websites.txt

#exit 0
#return echo $?


