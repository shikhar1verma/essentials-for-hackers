#!/usr/bin/env python
'''
this code will send the webserver a get request which the host can
understand and reply its banner in which we can have the information
about the host like the which webserver is this. After knowing version
on which webserver is running on we can check the vulnerabilities of that
webserver through google search'
'''

import socket       #importing the socket library


def conn(ip_address,port):                              #creating the connection and try to communicate with webserver in its langguage
    try:
        s=socket.socket()
        s.connect((ip_address,port))
	if port == 80:
	    gethttp(ip_address,s)                       #calling the function to get the sentence which can be understood by the webserver
	else:
            data = s.recv(1024)
            print ip_address + ':' + data
        s.close()
    except:
	    pass


def gethttp(ip_address,s):                                  #it will create the string or sentence that can be understood by the webserver
    try:
	s.send('GET HTTP/1.1\nHost: '+ip_address+'\n\n')    #sending the get request to the desired host
	ret= s.recv(1024)
	print ip_address + ':' + ret
	return
    except Exception,e:
	print 'error occured in grabbing'
	return


k = raw_input('enter the name of site to grab: ')       #user input of the ip or the domain name of the site user want to grab the banner
conn(k,80)                                              #calling the fubnction to create the tcp connection
