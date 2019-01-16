from subprocess import call
import os

# Instala el modulo de python termcolor para que el texto tenga color en la consola
call("pip install termcolor", shell = True)

# Instala el modulo de automatizacion pexpect para poder deshacernos de algunos prompts
call("pip install pexpect", shell = True)

# Añade la ultima version de ansible
call("sudo apt-add-repository -y ppa:ansible/ansible", shell = True)

# Actualiza los repositorios
call("sudo apt-get update", shell = True)

# Instala ansible
call("sudo apt-get -y install ansible", shell = True)

# Copia los ficheros de ansible que necesitamos a /etc/ansible
call ("sudo cp -r /home/upm/practica/ansible/roles  /etc/ansible/", shell = True)
call ("sudo cp -r /home/upm/practica/ansible/hosts  /etc/ansible/hosts", shell = True)
call ("sudo cp -r /home/upm/practica/ansible/playbook.yml  /etc/ansible/playbook.yml", shell = True)

# Se descarga el escenario virtual
call("wget http://idefix.dit.upm.es/cdps/pfinal/pfinal.tgz", shell = True)

# Descomprime el escenario virtual
call("sudo vnx --unpack /home/upm/practica/pfinal.tgz", shell = True)

# Cambiar de directorio y arrancar el escenario virtual
os.chdir("/home/upm/practica/pfinal")
call("bin/prepare-pfinal-vm", shell = True)
call("sudo vnx -f pfinal.xml --create", shell = True)

call('python /home/upm/practica/setup_scripts/rsaKeysSetup.py xxxx', shell = True)
