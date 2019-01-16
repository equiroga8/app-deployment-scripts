from subprocess import call
from termcolor import colored
from pexpect import *

virtualMachines = ['c1', 'c2', 'fw', 'lb', 's1', 's2', 's3', 'bbdd', 'nas1', 'nas2', 'nas3']

print colored("-> Creating 4096 bit private/public RSA keys. Press enter", 'green')
call('ssh-keygen -t rsa -b 4096', shell = True)

print colored("-> Copying generated public key to all virtual machines.", 'green')
for remoteServer in virtualMachines:
	run('ssh-copy-id -i /home/upm/.ssh/id_rsa.pub root@' + remoteServer, events = {'[P|p]assword': 'xxxx\n', 'Are you sure you want': 'yes\n'})
	print colored('-> Public key copied to /root/.ssh/authorized_keys on ' + remoteServer, 'green')
