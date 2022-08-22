# Puppet script to configure a web server

exec { 'apt update'
  command => 'apt update',
  path    => '/usr/bin/',
}

package {'nginx':
  ensure  => 'present',
}

file_line { 'add custom header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
