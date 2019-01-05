# Shard
*Raspberry Pi Zero WiFi RC Car*

#### Project path: /var/www/Shard

#### Enable SSH, SPI, change host name:
````
sudo raspi-config
````
    
#### Change password:
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

#### Install Apache SSL: https://wiki.debian.org/Self-Signed_Certificate
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

#### Change default webpage location:
````
sudo nano /etc/apache2/sites-available/000-default.conf
    DocumentRoot /var/www/Shard/templates
sudo nano /etc/apache2/sites-available/default-ssl.conf
    ServerName 192.168.1.X:443
    DocumentRoot /var/www/Shard/templates
````

#### Apache Security:
http://www.tecmint.com/apache-security-tips/
http://www.petefreitag.com/item/505.cfm

#### Install Motion: 
https://youtu.be/3m29S2rbqBw
#### Make it work with official RaspiCam:
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
````

#### Make Flask run through Apache SSL:
http://www.jakowicz.com/flask-apache-wsgi/
````
sudo cp Shard.service /lib/systemd/system/
ls - l /lib/systemd/system
sudo systemctl enable Shard.service
systemctl status Shard.service
````
