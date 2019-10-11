# Puppet manifest to fix nginx worker processes.
exec { 'workers':
    command => '/bin/sed -i "s/15/1500/g" /etc/default/nginx'
}
-> exec {'restart web server':
  command => '/usr/sbin/service nginx restart'
}
