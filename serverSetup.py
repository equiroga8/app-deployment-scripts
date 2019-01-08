#
#
# curl -sL https://deb.nodesource.com/setup_8.x | sudo bash -
# apt install nodejs
# git clone https://github.com/CORE-UPM/quiz_2019.git
# cd quiz_2019/
# mkdir public/uploads
# ln -s /root/quiz_2019/public/uploads/ /mnt/nas
# npm install
# npm install forever
# npm install mysql2
# export QUIZ_OPEN_REGISTER=yes
# export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31:3306/quiz
# npm run-script migrate_cdps
# npm run-script seed_cdps
#
# ./node_modules/forever/bin/forever start ./bin/www
#
# 


from subprocess import call
from termcolor import colored

servers = ['s1', 's2', 's3']

for server in servers:
	print colored("-> " + server + ": Updating nodejs repo" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- curl -sL https://deb.nodesource.com/setup_8.x | sudo bash -", shell = True)

	print colored("-> " + server + ": Installing nodejs and npm" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- apt-get -y install nodejs", shell = True)

	print colored("-> " + server + ": Cloning quiz_2019 repository" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git\"", shell = True)

	print colored("-> " + server + ": Creating quiz_2019/public/uploads folder" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- mkdir /root/quiz_2019/public/uploads", shell = True)

	print colored("-> " + server + ": Creating symbolic link between /public/uploads adn /mnt/nas" , 'green')	
	call("sudo lxc-attach --clear-env -n " + server + " -- ln -s /root/quiz_2019/public/uploads/ /mnt/nas", shell = True)

	print colored("-> " + server + ": Installing npm modules" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- bash -c \"cd /root/quiz_2019; npm install\"" , shell = True)

	print colored("-> " + server + ": Installing forever module" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- bash -c \"cd /root/quiz_2019; npm install forever\"" , shell = True)

	print colored("-> " + server + ": Installing mysql2 module" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- bash -c \"cd /root/quiz_2019; npm install mysql2\"" , shell = True)

	print colored("-> " + server + ": Opening register" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- bash -c \"cd /root/quiz_2019; export QUIZ_OPEN_REGISTER=yes\"" , shell = True)

	print colored("-> " + server + ": Connecting to bbdd" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- bash -c \"cd /root/quiz_2019; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31:3306/quiz\"" , shell = True)

print colored("-> Migrating database" , 'green')
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"cd quiz_2019; npm run-script migrate_cdps\"" , shell = True)

print colored("->  Generating default values for the database" , 'green')
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"cd quiz_2019; npm run-script seed_cdps\"" , shell = True)

for server in servers:
	print colored("-> " + server + ": Starting service on port 3000" , 'green')
	call("sudo lxc-attach --clear-env -n " + server + " -- bash -c \"cd quiz_2019; ./node_modules/forever/bin/forever start ./bin/www\"" , shell = True)	