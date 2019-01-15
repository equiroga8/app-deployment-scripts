# -- instalar en mv bbdd
# apt update 
# apt -y install mariadb-server
# sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf
# systemctl restart mysql
# mysqladmin -u root password xxxx
# mysql -u root --password='xxxx' -e "CREATE USER 'quiz' IDENTIFIED BY 'xxxx';"
# mysql -u root --password='xxxx' -e "CREATE DATABASE quiz;"
# mysql -u root --password='xxxx' -e "GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';"
# mysql -u root --password='xxxx' -e "GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';"
# mysql -u root --password='xxxx' -e "FLUSH PRIVILEGES;"

# -- Comprobar instalacion en s1
# apt -y install mariadb-client
# mysql -h 20.2.4.31 -u quiz --password='xxxx' quiz
# show databases;

from subprocess import call
from termcolor import colored
from pexpect import *

print colored("-> Updating VM", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- apt update", shell = True)

print colored("-> Installing mariadb-server", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- apt -y install mariadb-server", shell = True)

print colored("-> Step 1", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf", shell = True)

print colored("-> Step 2", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- systemctl restart mysql", shell = True)

print colored("-> Step 3", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysqladmin -u root password xxxx", shell = True)

print colored("-> Creating user quiz", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\"", shell = True)

print colored("-> Creating database", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\"", shell = True)

print colored("-> Step 6", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';\"", shell = True)

print colored("-> Step 7", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\"", shell = True)

print colored("-> Step 8", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\"", shell = True)

print colored("-> Verifying that the BBDD setup was successfull", 'blue')

print colored("-> Updating repositories on s1", 'green')
call("sudo lxc-attach --clear-env -n s1 -- apt-get update", shell = True)

print colored("-> Installing mariadb-client", 'green')
call("sudo lxc-attach --clear-env -n s1 -- apt -y install mariadb-client", shell = True)

print colored("-> Conecting to remote database. Type \"show databases;\" to verify that the database has been configured correctly", 'green')
call("sudo lxc-attach --clear-env -n s1 -- mysql -h 20.2.4.31 -u quiz --password='xxxx' quiz", shell = True)
#run('sudo lxc-attach --clear-env -n s1 -- mysql -h 20.2.4.31 -u quiz --password=\'xxxx\' quiz', events = {'[quiz]>': 'show databases;', '| quiz               |': 'quit'})

