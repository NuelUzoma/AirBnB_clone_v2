#!/usr/bin/env bash
# Write a Bash Script that sets up your web servers for the deployment of web_static

# Install nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow "Nginx HTTP"

# Create the folder /data/ if it doesnt exist
sudo mkdir -p /data/

#Create folder /data/web_static/ if it doesnt exist
sudo mkdir -p /data/web_static/

# Create this folder if it doesnt exist
sudo mkdir -p /data/web_static/shared/

# Create this folder if it doesnt exist
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file for Nginx configuration
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
    </html>" > sudo tee /data/web_static/releases/test/index.html

# Create a Symbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

sudo sed -i "/listen 80 default server/# location /hbnb_static (alias /data/web_static/current/;)" /etc/sites-enabled/default

sudo service nginx restart
