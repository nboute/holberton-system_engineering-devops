# Puppet script to configure a web server
package {'nginx':
  ensure => 'present',
}

file {'/var/www/html/index.nginx-debian.html':
  ensure => 'present',
  content => 'Hello world\n',
}

file_line { 'add redirect 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGU1wu4 permanent; }',
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],

}
