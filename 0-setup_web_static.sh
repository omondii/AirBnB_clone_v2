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
config_file="/etc/nginx/sites-available/default"
nginx_config="location /hbnb_static/ {
    alias $webstatic_dir/current/;
}"
if ! grep -q "$nginx_config" "$config_file"; then
	sudo sed -i "/server_name _;/a $nginx_config" "$config_file"
fi

sudo nginx -t
sudo systemctl restart nginx

echo "Succesfull configuration and update of Nginx"
