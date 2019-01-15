from subprocess import call
import os

call("pip install termcolor", shell = True)
call("pip install pexpect", shell = True)

call("wget http://idefix.dit.upm.es/cdps/pfinal/pfinal.tgz", shell = True)
call("sudo vnx --unpack /home/upm/practica/pfinal.tgz", shell = True)
os.chdir("/home/upm/practica/pfinal")
call("bin/prepare-pfinal-vm", shell = True)
call("sudo vnx -f pfinal.xml --create", shell = True)

