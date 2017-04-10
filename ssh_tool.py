#!/usr/bin/python

import paramiko

hostname = '172.25.164.200'
user = 'sgrosu'
passw = ''
port = 22

if __name__ == "__main__":
	paramiko.util.log_to_file('paramiko.log')
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.connect(hostname,port,user,passw)
	stdin,stdout,stderr = s.exec_command("ifconfig eth0")
	print stdout.read()
	print stderr.read()
	s.close()
