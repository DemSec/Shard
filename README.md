# Shard
*Raspberry Pi Zero WiFi RC Car*

__Project path: /var/www/Shard__

__Enable SSH, SPI, change host name:__
''''
sudo raspi-config
''''
    
__Change password:__
sudo passwd <user>

__Update your installer and Upgrade your Raspibian (will take a long while)__
sudo apt-get update
sudo apt-get upgrade

__(Python and GPIO is pre-installed)__

__A similar project made by Sparkfun:__ https://www.youtube.com/watch?v=L55QYFnnrgo

__Install Flask:__ http://flask.pocoo.org/
http://mattrichardson.com/Raspberry-Pi-Flask/

sudo apt-get install python-pip
sudo pip install flask

Install Apache SSL: https://wiki.debian.org/Self-Signed_Certificate
sudo apt-get install apache2
sudo apt-get install apache2 openssl
sudo mkdir -p /etc/ssl/localcerts 
sudo openssl req -new -x509 -days 365 -nodes -out /etc/ssl/localcerts/apache.pem -keyout /etc/ssl/localcerts/apache.key
    FQDN: 192.168.1.X
sudo chmod 600 /etc/ssl/localcerts/apache*
(man openssl)
sudo a2enmod ssl
sudo nano /etc/apache2/sites-available/default-ssl.conf
    ServerName 192.168.1.X:443
    (or:
    NameVirtualHost 192.168.1.X:443
    <VirtualHost 192.168.1.X:443>)
    SSLEngine On
    SSLCertificateFile /etc/ssl/localcerts/apache.pem
    SSLCertificateKeyFile /etc/ssl/localcerts/apache.key
sudo a2ensite sitename
(port 443 is open by defauld in: /etc/apache2/ports.conf)
sudo service apache2 restart
https://127.0.0.1 (or https://192.168.1.X)

(python-pip is installed by default)

Change default webpage location:
sudo nano /etc/apache2/sites-available/000-default.conf
    DocumentRoot /var/www/Shard/templates
sudo nano /etc/apache2/sites-available/default-ssl.conf
    ServerName 192.168.1.14:443
    DocumentRoot /var/www/Shard/templates


Apache Security:
http://www.tecmint.com/apache-security-tips/
http://www.petefreitag.com/item/505.cfm

Install Motion:
https://youtu.be/3m29S2rbqBw
to make it work with official RaspiCam:
https://raspberrypi.stackexchange.com/questions/10480/raspi-camera-board-and-motion#26386

Install the Python server:

Make it a service to run at boot:
sudo cp Shard.service /lib/systemd/system/
sudo systemctl enable Shard.service

Make Flask run through Apache SSL:
http://www.jakowicz.com/flask-apache-wsgi/

Make it a Service (/var/www/Shard.service):
https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer/systemd-writing-and-enabling-a-service

[Unit]
Description= Shard car Control

[Service]
ExecStart=/usr/bin/python /var/www/Shard/main.py

[Install]
WantedBy=multi-user.target

sudo cp Shard.service /lib/systemd/system/
ls - l /lib/systemd/system
sudo systemclt enable Shard.service
systemctl status Shard.service
