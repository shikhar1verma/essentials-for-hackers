#!/usr/bin/python
'''
this code is used to scan the desired system's TCP
ports using the connect scan. It tells only the
given ports are opened or closed
'''
import socket           #import all methods from socket
from socket import *


                                                                # function which scans the remote system for opened ports
def connScan(IP,Port):
	try:
        	sock = socket(AF_INET, SOCK_STREAM)
        	sock.settimeout(0.5)
        	sock.connect((IP, Port))
    	except error :
		return False
	return True


IP= str(raw_input("Input the host to be scanned: "))            #it gves the user input of the host ip you want to scan

port_list = str(raw_input("Enter the comma seperated list of ports to be scanned: "))       #user input of the list of ports


tgtPorts = port_list.split(',')                                 #list of ports

if (IP == '') | (port_list == ''):                              #checking the ports and ip is given by the user
	print '[-] You must specify a target host and port[s].'
        exit(0)

for tgtPort in tgtPorts:                                                    #it will check the specified ports one by one
	print 'Scanning port :',tgtPort
	r=connScan(IP, int(tgtPort))                                        #calling the function wich actually check if the port opened or closed
	if r==True:
		print '[+]...............tcp Port %s is open'%tgtPort
	else:
		print '[-]...............tcp Port %s is closed'%tgtPort
