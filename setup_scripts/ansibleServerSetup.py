
from pexpect import *
from subprocess import call

call('ansible-playbook -K /etc/ansible/playbook.yml', shell = True)
