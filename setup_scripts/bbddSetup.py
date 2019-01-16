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

print colored("-> Updating VM", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- apt update", shell = True)

print colored("-> Installing mariadb-server", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- apt -y install mariadb-server", shell = True)

print colored("-> Modifying /etc/mysql/mariadb.conf.d/50-server.cnf", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf", shell = True)

print colored("-> Restarting mysql service", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- systemctl restart mysql", shell = True)

print colored("-> Setting access credentials", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysqladmin -u root password xxxx", shell = True)

print colored("-> Creating user quiz", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\"", shell = True)

print colored("-> Creating database quiz", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\"", shell = True)

print colored("-> Granting all privileges to user quiz on database quiz from bbdd", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';\"", shell = True)

print colored("-> Granting all privileges to user quiz on database quiz from any remote server", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\"", shell = True)

print colored("-> Refreshing privileges", 'green')
call("sudo lxc-attach --clear-env -n bbdd -- mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\"", shell = True)


