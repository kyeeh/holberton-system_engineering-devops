# Puppet manifest to fix misconfiguration in Wordpress
exec { 'no phpp':
    command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
