#!/usr/bin/env python
'''
this code is used to scan the ports of remote system.
The scanning of tcp ports is done with nmap library of
python.
'''
import nmap         #library for scanning the ports
import pdb          #to check the python script line bt line (python debugger)

def nmapScan(tgtHost, tgtPort):                             #this function will scan and check the service running on that port
    nmScan = nmap.PortScanner()                             #PortScanner class is called and object 'nmScan' is made
    nmScan.scan(tgtHost, tgtPort)
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']     #it will tell the state of port (open,closed,filtered)
    print " [*] " + tgtHost + " tcp/"+tgtPort +" "+state

def main():                                                                             #the main def of the code
    tgtHost = str(raw_input("Input the host to be scanned: "))                          #user input of ip of host
    tgtPorts = str(raw_input("Enter the comma separated list of ports to be scanned: "))#user input of ports of host to be scanned
    tgtPorts = tgtPorts.split(',')
    if (tgtHost == '') | (tgtPorts == ''):                                              #to check if both ip and ports are specified or not
        print 'enter both port and host IP'
        exit(0)
    for tgtPort in tgtPorts:                                                            #checking all the ports one by one
        nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':      #the codes starts from here
    main()
