#
# gluster peer probe 20.2.4.22
# gluster peer probe 20.2.4.23
# gluster peer status
# gluster volume create nas replica 3 20.2.4.21:/nas 20.2.4.22:/nas 20.2.4.23:/nas force
# gluster volume start nas
# gluster volume set nas network.ping-timeout 5
# - hacer de s1-3
# mkdir /mnt/nas
# mount -t glusterfs 20.2.4.21:/nas /mnt/nas

from subprocess import call
from termcolor import colored

print colored("-> Configuring nas2 as peer", 'green')
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.2.4.22", shell = True)

print colored("-> Configuring nas3 as peer", 'green')
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 20.2.4.23", shell = True)

print colored("-> Verifying peer status", 'green')
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer status", shell = True)

print colored("-> Creating new volume nas", 'green')
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume create nas replica 3 20.2.4.21:/nas 20.2.4.22:/nas 20.2.4.23:/nas force", shell = True)

print colored("-> Starting volume nas", 'green')
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume start nas", shell = True)

print colored("-> Modifying volume nas timeout", 'green')
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume set nas network.ping-timeout 5", shell = True)

for x in range (1,4):
	print colored("-> Creating directory /mnt/nas and conection to the volume on s" + str(x) , 'green')
	call("sudo lxc-attach --clear-env -n s" + str(x) + " -- mkdir /mnt/nas", shell = True)
	call("sudo lxc-attach --clear-env -n s" + str(x) + " -- mount -t glusterfs 20.2.4.21:/nas /mnt/nas", shell = True)


