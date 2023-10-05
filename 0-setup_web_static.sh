#!/usr/bin/env bash

# Installing nginx if its not installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx is installed"
else
    sudo apt-get update
    sudo apt-get install -y nginx
    echo "Nginx successfully installed"
fi

# Create the neccessary directories
data_dir='/data/'
webstatic_dir='/data/web_static/'
releases_dir='/data/web_static/releases/'
shared_dir='/data/web_static/shared/'
tests_dir='/data/web_static/releases/test'

# for each dir above, chheck if exits, if not, create it
if [ ! -d "$data_dir" ]; then
    sudo mkdir -p "$data_dir"
    echo "Succesfully Created: $data_dir"
fi

if [ ! -d "$webstatic_dir" ]; then
    sudo mkdir -p "$webstatic_dir"
    echo "Succesfully Created: $webstatic_dir"
fi

if [ ! -d "$releases_dir" ]; then
    sudo mkdir -p "$releases_dir"
    echo "Successfully Created: $releases_dir"
fi

if [ ! -d "$shared_dir" ]; then
    sudo mkdir -p "$shared_dir"
    echo "Succesfully Created: $shared_dir"
fi

if [ ! -d "$tests_dir" ]; then
    sudo mkdir -p "$tests_dir"
    echo "Succesfully Created: $tests_dir"
fi

# Create a fake html file to test Nginx config
sudo bash -c "echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html"

# Symbolic link manipulation
# If currrent exists, delete it
current_link='/data/web_static/current'
if [ -L "$current_link" ]; then
    sudo rm -f $current_link
fi

# Create a new symbolic link to the tests_dir folder
sudo ln -s $tests_dir $current_link
echo 'Symbolic link created succesfully'

# Change ownership of /data/
sudo chown -R ubuntu:ubuntu /data/
echo 'Ownership permissions changed'

# Nginx server config.
# serve the content of /data/web_static/current/ to hbnb_static
config_file='/etc/nginx/sites-available/web_static'
if [ -f $config_file ]; then
    echo "server {
      listen *:80;
      location /hbnb_static/ {
      	       alias $webstatic_dir/current/;
      }
      location / {
      	       add_header X-served-By $HOSTNAME;
	       root /usr/share/nginx/html;
      }
 }" | sudo tee $config_file > /dev/null
    sudo ln -sf $config_file '/etc/nginx/sites-enabled/'
    echo 'Nginx configuration created and enabled'
fi

sudo nginx -t
sudo systemctl reload nginx

echo "Succesfull configuration and update of Nginx"
