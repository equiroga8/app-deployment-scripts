from subprocess import call
import os

call("pip install termcolor", shell = True)
call("pip install pexpect", shell = True)
call("sudo apt-add-repository -y ppa:ansible/ansible", shell = True)
call("sudo apt-get update", shell = True)
call("sudo apt-get -y install ansible", shell = True)
call ("sudo mv -f /home/upm/practica/ansible/roles  /etc/ansible/", shell = True)
call ("sudo mv -f /home/upm/practica/ansible/hosts  /etc/ansible/hosts", shell = True)
call ("sudo mv -f /home/upm/practica/ansible/playbook.yml  /etc/ansible/playbook.yml", shell = True)

call("wget http://idefix.dit.upm.es/cdps/pfinal/pfinal.tgz", shell = True)
call("sudo vnx --unpack /home/upm/practica/pfinal.tgz", shell = True)
os.chdir("/home/upm/practica/pfinal")
call("bin/prepare-pfinal-vm", shell = True)
call("sudo vnx -f pfinal.xml --create", shell = True)

call('python /home/upm/practica/setup_scripts/rsaKeysSetup.py xxxx', shell = True)
