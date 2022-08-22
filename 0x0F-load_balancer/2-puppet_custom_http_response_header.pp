# Puppet script to configure a web server

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => 'present',
  name    => 'nginx',
  require => Exec['apt update']
}

file_line { 'add custom header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
