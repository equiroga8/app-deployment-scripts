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