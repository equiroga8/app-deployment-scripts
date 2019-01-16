
from subprocess import call
from termcolor import colored


servers = ['s1', 's2', 's3']

for server in servers:

	print colored("-> Starting service on " + server + ". Type 'forever start ./bin/www'" , 'green')
	call("ssh -X -t root@"+ server +" \"cd /root/quiz_2019 ; bash\"", shell = True)
