#!/bin/bash

# Initial install script for pi-detector
# By Anton
# 03/14/17

echo '[+] Updating and installing dependencies...'
apt-get update && apt-get -y upgrade

echo '[+] Freeing up space. Removing Wolfram-Engine...'
apt-get purge wolfram-engine

apt-get install -y build-essential python-setuptools python-pip awscli

pip install boto3 watchdog simplejson PiCamera
rm -rf ~/.cache/pip

echo '[+] Configuring AWS...'
aws configure

cd

echo '[+] Installing Pi motion sensor module...'
curl -L https://raw.github.com/pageauc/pi-timolo/master/source/pi-timolo-install.sh | bash
mv $HOME/pi-timolo /home/pi/pi-timolo
mv $HOME/pi-detector /home/pi/pi-detector
chown -R pi:pi /home/pi/pi-timolo
chown -R pi:pi /home/pi/pi-detector

echo '[+] Adding auto launch for pi-timolo to start on boot'
sed -i "\$i su pi -c \"/home/pi/pi-timolo/pi-timolo.sh start > /dev/null &\"" /etc/rc.local
sed -i "\$i su pi -c \"/home/pi/pi-timolo/webserver.sh start > /dev/null &\"" /etc/rc.local
sed -i "\$i su pi -c \"/home/pi/pi-detector/watch.sh start > /dev/null &\"" /etc/rc.local

echo '[+] Adding cronjob and changing file permissions...'
chmod -R +x /home/pi/pi-detector
crontab -l > picron
echo "*/5 * * * * /home/pi/pi-detector/scripts/checkstart.sh" >> picron
crontab picron
rm picron

echo '[+] Done!'

exit 0

