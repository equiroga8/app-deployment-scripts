from subprocess import call
from termcolor import colored

print colored("---------------------------------", 'yellow')

print colored("-> Starting bbdd setup", 'cyan')
call('python /home/upm/practica/setup_scripts/bbddSetup.py', shell = True)
print colored("-> bbdd setup finished", 'cyan')

print colored("---------------------------------", 'yellow')

print colored("-> Starting lb setup", 'cyan')
call('python /home/upm/practica/setup_scripts/lbSetup.py', shell = True)
print colored("-> lb setup finished", 'cyan')

print colored("---------------------------------", 'yellow')

print colored("-> Starting fw setup", 'cyan')
call('python /home/upm/practica/setup_scripts/fwSetup.py', shell = True)
print colored("-> fw setup finished", 'cyan')

print colored("---------------------------------", 'yellow')

print colored("-> Starting server setup with ansible. Type the password", 'cyan')
call('python /home/upm/practica/setup_scripts/ansibleServerSetup.py', shell = True)
print colored("-> server setup finished", 'cyan')

print colored("---------------------------------", 'yellow')

print colored("-> Starting nas setup", 'cyan')
call('python /home/upm/practica/setup_scripts/nasSetup.py', shell = True)
print colored("-> nas setup finished", 'cyan')

print colored("---------------------------------", 'yellow')

print colored("-> Starting service", 'cyan')
call('python /home/upm/practica/setup_scripts/startForever.py', shell = True)
print colored("-> Service Started", 'cyan')