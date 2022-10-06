#Increases file limit for nginx

exec { 'limit_replace':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
}

service { 'nginx':
    ensure    => running,
    subscribe => Exec['limit_replace'],
}
