#!/bin/sh

# wget  https://raw.githubusercontent.com/xmayeur/spammon/master/SpamMon.conf
echo  "remove and stop existing container"
docker rm -f myip
echo "pull the latest version"
docker pull xmayeur/myip
echo "run the container"
docker run --name myip --restart always -v /root/:/conf/ -v /var/log:/var/log/ xmayeur/myip &
sleep 16
echo "bye-bye"