#! bash

sudo apt update -y
sudo apt upgrade -y
sudo apt install fail2ban -y


# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
# 16.04
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt update -y
sudo apt install mongodb-org-shell=3.6.5 mongodb-org-tools=3.6.5 -y

# Install some OS dependencies:
sudo apt-get install --no-install-recommends -y -q build-essential git python3-dev python3-venv
sudo apt-get install --no-install-recommends -y -q python3-pip wget
sudo apt-get install --no-install-recommends -y -q unzip
sudo apt-get install --no-install-recommends -y -q nginx
# for gzip support in uwsgi
sudo apt-get install --no-install-recommends -y -q libpcre3-dev libz-dev nload


# Basic git setup
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=720000'

git config --global user.email "you@email.com"
git config --global user.name "Your name"

# Web app file structure
sudo mkdir /apps
sudo chmod 777 /apps
mkdir /apps/logs
mkdir /apps/logs/pypi_web
mkdir /apps/logs/pypi_web/app_log
cd /apps

# Create a virtual env for the app.
cd /apps
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools httpie


# clone the repo:
cd /apps
git clone https://github.com/mikeckennedy/build-pypi-mongodb-webcast-series.git

# Setup the web app:
cd /apps/build-pypi-mongodb-webcast-series/part3/webapp/final/pypi_web_mongodb_f
pip install -r requirements.txt

# Copy and enable the daemon
sudo cp /apps/build-pypi-mongodb-webcast-series/part3/server_config/pypi.service /etc/systemd/system/


sudo systemctl start pypi
sudo systemctl status pypi
sudo systemctl enable pypi

# Setup the public facing server (NGINGX)

# CAREFUL HERE. If you are using default, maybe skip this
sudo rm /etc/nginx/sites-enabled/default

sudo cp /apps/build-pypi-mongodb-webcast-series/part3/server_config/pypi.nginx /etc/nginx/sites-enabled/pypi.nginx
