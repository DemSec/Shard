# Shard
*Raspberry Pi Zero WiFi RC Car*

#### Project path: /var/www/Shard

#### Flash a Desktop verison of Raspibian to 8GB SD card:
https://www.raspberrypi.org/downloads/raspbian/

#### If using RPi Zero, create an 'ssh' file to boot to enable SSH
#### At the very bottom of 'config.txt', add:
````
dtoverlay=dwc2
````

#### In 'cmdline.txt', after 'rootwait', add:
````
modules-load=dwc2,g_ether
````

#### Now, load the SD card and connect to computer through microUSB hub

#### Download iTunes:
https://www.apple.com/itunes/download/
#### Change the extention of iTunes64Setup.exe to .rar
#### Unzip and run Bonjour64.msi, this installs Bonjour v3.0, the newest version available
#### This allows PuTTY to connect through <hostname\>.local IP addresses

#### Enable SSH, VNC, change host name and password:
````
sudo raspi-config
````
    
#### Or change password via command line:
````
sudo passwd <user>
````

#### Update your installer and Upgrade your Raspibian (will take a long while):
````
sudo apt-get update
sudo apt-get upgrade
````

#### (Python and GPIO is pre-installed)

#### A similar project made by Sparkfun: https://www.youtube.com/watch?v=L55QYFnnrgo

#### Install Flask: http://flask.pocoo.org/
http://mattrichardson.com/Raspberry-Pi-Flask/
````
sudo apt-get install python-pip
sudo pip install flask
````

#### (SKIP) Install Apache SSL: https://wiki.debian.org/Self-Signed_Certificate
````
sudo apt-get install apache2
sudo apt-get install openssl
sudo mkdir -p /etc/ssl/localcerts 
sudo openssl req -new -x509 -days 365 -nodes -out /etc/ssl/localcerts/apache.pem -keyout /etc/ssl/localcerts/apache.key
    FQDN: 192.168.1.X
sudo chmod 600 /etc/ssl/localcerts/apache*
(man openssl)
sudo a2enmod ssl
sudo nano /etc/apache2/sites-available/default-ssl.conf
    ServerName 192.168.1.X:443 # I don't know what this does...
    SSLEngine On # Make sure this is on
    SSLCertificateFile /etc/ssl/localcerts/apache.pem
    SSLCertificateKeyFile /etc/ssl/localcerts/apache.key
(I don't what what this does either)
sudo a2ensite sitename
(port 443 is open by default in: /etc/apache2/ports.conf)
sudo service apache2 restart
Browse to https://192.168.1.X
````

#### (python-pip is installed by default)

#### (SKIP) Change default webpage location:
````
sudo nano /etc/apache2/sites-available/000-default.conf
    DocumentRoot /var/www/Shard/templates
sudo nano /etc/apache2/sites-available/default-ssl.conf
    ServerName 192.168.1.X:443
    DocumentRoot /var/www/Shard/templates
````

#### (SKIP) Apache Security:
http://www.tecmint.com/apache-security-tips/
http://www.petefreitag.com/item/505.cfm

#### (SKIP) Install Motion: 
https://youtu.be/3m29S2rbqBw

#### RaspiCam to USB /dev/video0 conversion:
https://raspberrypi.stackexchange.com/questions/10480/raspi-camera-board-and-motion#26386

#### Now, clone this repository at /var/www/Shard
````
sudo git clone https://github.com/DemSec/Shard.git /var/www/Shard
````
#### Make the repository into a service that runs on boot:
https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer/systemd-writing-and-enabling-a-service
````
sudo cp /var/www/Shard/Shard.service /lib/systemd/system/
sudo systemctl enable Shard.service
(ls - l /lib/systemd/system)
(systemctl status Shard.service)
````

#### (SKIP) Make Flask run through Apache SSL:
http://www.jakowicz.com/flask-apache-wsgi/

#### Simple Guide to GIT:
https://rogerdudler.github.io/git-guide/
````
sudo git config --global user.email "email"
sudo git add *
sudo git commit -m "message"
sudo git push origin master
````
````
sudo git pull
````

#### Download and Install mjpg-streamer:
https://github.com/jacksonliam/mjpg-streamer
#### (TODO) Make it a service that runs on boot
