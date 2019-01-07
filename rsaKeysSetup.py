from subprocess import call
from termcolor import colored
import pexpect

virtualMachines = ["c1", "c2", "fw", "lb", "s1", "s1", "s3", "bbdd", "nas1", "nas2", "nas3"]

print colored("-> Creating 4096 bit pairwise RSA key. Press enter", 'green')
call("ssh-keygen -t rsa -b 4096", shell = True)

print colored("-> Copying RSA public key to all virtual machines.", 'green')
for remoteServer in virtualMachines:
	#call("ssh-copy-id -i /home/upm/.ssh/id_rsa.pub root@" + remoteServer, shell = True)
	child = pexpect.spawn('ssh-copy-id -i /home/upm/.ssh/id_rsa.pub root@' + remoteServer)
	child.expect("root@" + remoteServer + "'s password:")
	child.sendline('xxxx')
