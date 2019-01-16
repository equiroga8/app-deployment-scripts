
from pexpect import *
from subprocess import call

call('ansible-playbook /etc/ansible/playbook.yml', shell = True)
