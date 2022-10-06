# Set open file limit for user holberton
exec { 'hard limit':
    command => '/bin/sed -i "s/holberton hard nofile 5/holberton hard nofile 4096/" /etc/security/limits.conf',
}

exec { 'soft limit':
    command => '/bin/sed -i "s/holberton soft nofile 4/holberton soft nofile 1024/" /etc/security/limits.conf',
}
