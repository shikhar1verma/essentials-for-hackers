#!/usr/bin/env python
'''
This code is for ssh (secure shell) bot.
if we want to take the control of remote
computer automatically.Through this script
you can send the commands from your computer
to the host computer.In this script i assume
that you already cracked the password and the username
of the remote computer. In this script where you have to
put the password youo can put the dictionary of passwords
to crack the password and print the password. And then
send your commands.
'''

import pexpect              #this library will automating interactive applications such as ssh, ftp, passwd, telnet, etc
                            #it will spawn a child application and control it as if a human were typing commands

PROMPT = ['# ', '>>> ', '> ', '\$ ']        #different interactive shells have different prompt symbols

def send_command(child, cmd):       #it will send the desired command and print the command result in our terminal
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):                                      #this function will get the host ip, username and password
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child=pexpect.spawn(connStr)                                        #Call a method of pexpect to spawn a connection to host and get the output in object-child
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:                                                        #if timeout happen means no response
        print '[-] Error Connecting'
        return
    if ret == 1:                                                        # if first tme this is happenening then it will ask for a key
	child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:                                                    #after then timeout can also happen
            print '[-] Error Connecting'
            return
    child.sendline(password)                                            #then after first two condition this will always happen sending the required password
    child.expect(PROMPT)
    return child

def main():
    host = '192.168.1.2'                                    #code to input host ip address
    user = 'user'                                           #host username input
    password = 'password'                                   #host user password input
    child = connect(user, host, password)                   #call the connect function
    send_command(child, 'ls')                               #call the function send_command to send the command to remote system

if __name__ == '__main__':      #code starts from here
    main()

