# service apache2 stop
# apt-get -y install haproxy
# scp /home/upm/Desktop/haproxy.cfg root@lb:/etc/haproxy/haproxy.cfg
# sudo service haproxy restart

from subprocess import call
from termcolor import colored

print colored("-> Updating VM", 'green')
call("sudo lxc-attach --clear-env -n lb -- apt-get update", shell = True)

print colored("-> Stopping apache service", 'green')
call("sudo lxc-attach --clear-env -n lb -- service apache2 stop", shell = True)

print colored("-> Installing HAProxy", 'green')
call("sudo lxc-attach --clear-env -n lb -- apt-get -y install haproxy", shell = True)

print colored("-> Copying HAProxy configuration file.", 'green')
call("scp /home/upm/practica/cfg_files/haproxy.cfg root@lb:/etc/haproxy/haproxy.cfg", shell = True)

print colored("-> Restarting HAProxy service", 'green')
call("sudo lxc-attach --clear-env -n lb -- service haproxy restart", shell = True)