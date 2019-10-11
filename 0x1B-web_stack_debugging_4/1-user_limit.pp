# Puppet manifest to fix open file limits.
exec { 'soft':
    command => '/bin/sed -i "holberton soft nofile 4/holberton hard nofile 1500/" /etc/security/limits.conf'
}
exec { 'hard':
    command => '/bin/sed -i "holberton hard nofile 5/holberton hard nofile 1500/" /etc/security/limits.conf'
}
-> exec {'reload':
  command => '/usr/sbin/sysctl -p'
}
