# Install Nginx web server with custom header response
exec { '/usr/bin/env apt-get update -y': }
exec { '/usr/bin/env apt-get install nginx -y': }
exec { '/usr/bin/env header="\\\tadd_header X-Served-By $HOSTNAME;\n"': }
exec { '/usr/bin/env sudo sed -i "38i $header" /etc/nginx/sites-available/default': }
exec { '/usr/bin/env sudo service nginx restart':}
