from subprocess import call
import os

call("pip install termcolor", shell = True)
call("pip install pexpect", shell = True)
call("sudo apt-add-repository ppa:ansible/ansible", shell = True)
call("sudo apt-get update", shell = True)
call("sudo apt-get -y install ansible", shell = True)
call ("sudo cp /home/upm/practicas/roles  /etc/ansible/roles")
call ("sudo cp /home/upm/practicas/hosts  /etc/ansible/hosts")
call ("sudo cp /home/upm/practicas/playbook.yml  /etc/ansible/playbook.yml")

call("wget http://idefix.dit.upm.es/cdps/pfinal/pfinal.tgz", shell = True)
call("sudo vnx --unpack /home/upm/practica/pfinal.tgz", shell = True)
os.chdir("/home/upm/practica/pfinal")
call("bin/prepare-pfinal-vm", shell = True)
call("sudo vnx -f pfinal.xml --create", shell = True)


call('python /home/upm/practica/setup_scripts/rsaKeysSetup.py', shell = True)