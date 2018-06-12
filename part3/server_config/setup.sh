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



# Mongo user:
# pypi_db_admin
# 8hw8fxrtDVNd6tvtCRczEJ)oVuaaeUk6