# Puppet script to configure a web server

include apt

package {'nginx':
  ensure  => 'present',
  require => Class['apt::update']
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
