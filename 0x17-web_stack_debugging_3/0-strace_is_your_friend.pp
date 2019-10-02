# Puppet manifest to fix misconfiguration in Wordpress
exec { 'no phpp':
    command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
exec {'restart web server':
  command => '/usr/sbin/service apache2 restart'
}
