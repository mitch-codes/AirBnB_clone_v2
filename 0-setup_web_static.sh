#!/bin/bash

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "this is a test" >> /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
awk '!/^#/' /etc/nginx/sites-available/default > /etc/nginx/sites-available/def2
sed '/server_name/a\\location /data/web_static/current/ {alias hbnb_static;}' /etc/nginx/sites-available/def2 > /etc/nginx/sites-available/def3
mv /etc/nginx/sites-available/def3  /etc/nginx/sites-available/default
rm /etc/nginx/sites-available/def2
sudo service nginx restart
