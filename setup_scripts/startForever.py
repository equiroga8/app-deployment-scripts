
from subprocess import call
from termcolor import colored


servers = ['s1', 's2', 's3']

for server in servers:

	print colored("-> Starting service on " + server + ". Change Directory to 'quiz_2019' and type 'forever start ./bin/www'" , 'green')
	call("ssh -X root@"+ server, shell = True)
