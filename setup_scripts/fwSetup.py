# -- copia del fichero fw.fw al la mv fw
# scp /home/upm/Desktop/fw.fw root@fw:/root/fw.fw
# -- ejecucion del script fw.fw
# sudo lxc-attach --clear-env -n fw -- /root/./fw.fw
# -- comprobaciones para ver si se ha configurado correctamente
# ping -c3 20.2.3.11 (ping a s1 no deberia funcionar)
# ping -c3 20.2.1.1 (ping a fw no deberia funcionar)
# ping -c3 20.2.2.2 (ping a lb si deberia funcionar)

from subprocess import call
from termcolor import colored

print colored("-> Copying firewall configuration file to fw VM.", 'green')
call("scp /home/upm/practica/cfg_files/fw.fw root@fw:/root/fw.fw", shell = True)

print colored("-> Executing firewall configuration file", 'green')
call("sudo lxc-attach --clear-env -n fw -- /root/./fw.fw", shell = True)

print colored("-> Pinging s1 (Should return no response)", 'green')
call("ping -c3 20.2.3.11", shell = True)
print colored("-> Pinging fw (Should return no response)", 'green')
call("ping -c3 20.2.1.1", shell = True)
print colored("-> Pinging lb (Should return response)", 'green')
call("ping -c3 20.2.2.2", shell = True)
